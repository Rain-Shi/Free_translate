"""
性能优化器 - 提升翻译速度
"""

import time
from typing import List, Dict, Any
import streamlit as st

class PerformanceOptimizer:
    """性能优化器"""
    
    def __init__(self):
        self.cache = {}  # 翻译缓存
        self.batch_size = 5  # 批处理大小
        self.max_retries = 3  # 最大重试次数
    
    def optimize_translation_process(self, content_items: List[Dict], target_lang: str, translator) -> List[Dict]:
        """优化翻译流程"""
        st.info("🚀 启用性能优化模式...")
        
        # 1. 批量预处理
        st.info("📦 批量预处理内容...")
        processed_items = self._batch_preprocess(content_items)
        
        # 2. 智能缓存检查
        st.info("💾 检查翻译缓存...")
        cached_items, uncached_items = self._check_cache(processed_items)
        
        # 3. 批量翻译
        if uncached_items:
            st.info(f"🔄 批量翻译 {len(uncached_items)} 项内容...")
            translated_items = self._batch_translate(uncached_items, target_lang, translator)
            
            # 更新缓存
            self._update_cache(translated_items)
        else:
            translated_items = []
        
        # 4. 合并结果
        all_translated = cached_items + translated_items
        
        # 5. 性能统计
        self._show_performance_stats(len(content_items), len(cached_items), len(translated_items))
        
        return all_translated
    
    def _batch_preprocess(self, content_items: List[Dict]) -> List[Dict]:
        """批量预处理内容"""
        processed_items = []
        
        for item in content_items:
            # 预处理文本
            processed_item = {
                **item,
                'processed_text': item.get('text', '').strip(),
                'text_length': len(item.get('text', '')),
                'is_short': len(item.get('text', '')) < 50,
                'is_long': len(item.get('text', '')) > 200
            }
            processed_items.append(processed_item)
        
        return processed_items
    
    def _check_cache(self, items: List[Dict]) -> tuple:
        """检查翻译缓存"""
        cached_items = []
        uncached_items = []
        
        for item in items:
            text_key = item.get('processed_text', '')
            cache_key = f"{text_key}_{item.get('type', '')}"
            
            if cache_key in self.cache:
                # 使用缓存
                cached_item = {**item, 'translated_text': self.cache[cache_key]}
                cached_items.append(cached_item)
            else:
                # 需要翻译
                uncached_items.append(item)
        
        return cached_items, uncached_items
    
    def _batch_translate(self, items: List[Dict], target_lang: str, translator) -> List[Dict]:
        """批量翻译"""
        translated_items = []
        
        # 按长度分组
        short_items = [item for item in items if item.get('is_short', False)]
        long_items = [item for item in items if item.get('is_long', False)]
        medium_items = [item for item in items if not item.get('is_short', False) and not item.get('is_long', False)]
        
        # 短文本批量处理
        if short_items:
            translated_items.extend(self._translate_short_texts(short_items, target_lang, translator))
        
        # 中等长度文本
        if medium_items:
            translated_items.extend(self._translate_medium_texts(medium_items, target_lang, translator))
        
        # 长文本单独处理
        if long_items:
            translated_items.extend(self._translate_long_texts(long_items, target_lang, translator))
        
        return translated_items
    
    def _translate_short_texts(self, items: List[Dict], target_lang: str, translator) -> List[Dict]:
        """翻译短文本（批量）"""
        if not items:
            return []
        
        # 合并短文本进行批量翻译
        combined_text = " | ".join([item.get('processed_text', '') for item in items])
        
        try:
            # 批量翻译
            translated_combined = translator._translate_paragraph_simple(combined_text, target_lang)
            
            # 分割结果
            translated_parts = translated_combined.split(" | ")
            
            translated_items = []
            for i, item in enumerate(items):
                translated_text = translated_parts[i] if i < len(translated_parts) else item.get('processed_text', '')
                translated_items.append({
                    **item,
                    'translated_text': translated_text
                })
            
            return translated_items
            
        except Exception as e:
            st.warning(f"批量翻译短文本失败: {str(e)}")
            # 回退到单独翻译
            return self._translate_individually(items, target_lang, translator)
    
    def _translate_medium_texts(self, items: List[Dict], target_lang: str, translator) -> List[Dict]:
        """翻译中等长度文本"""
        return self._translate_individually(items, target_lang, translator)
    
    def _translate_long_texts(self, items: List[Dict], target_lang: str, translator) -> List[Dict]:
        """翻译长文本"""
        return self._translate_individually(items, target_lang, translator)
    
    def _translate_individually(self, items: List[Dict], target_lang: str, translator) -> List[Dict]:
        """单独翻译每个项目"""
        translated_items = []
        
        for i, item in enumerate(items):
            try:
                # 显示进度
                if i % 5 == 0:
                    st.info(f"正在翻译第 {i+1}/{len(items)} 项...")
                
                # 翻译
                if item.get('type') == 'paragraph':
                    translated_text = translator._translate_paragraph_simple(item.get('processed_text', ''), target_lang)
                elif item.get('type') == 'table_cell':
                    translated_text = translator._translate_table_cell_simple(item.get('processed_text', ''), target_lang)
                else:
                    translated_text = item.get('processed_text', '')
                
                translated_items.append({
                    **item,
                    'translated_text': translated_text
                })
                
            except Exception as e:
                st.warning(f"翻译第 {i+1} 项失败: {str(e)}")
                translated_items.append({
                    **item,
                    'translated_text': item.get('processed_text', '')
                })
        
        return translated_items
    
    def _update_cache(self, translated_items: List[Dict]):
        """更新缓存"""
        for item in translated_items:
            text_key = item.get('processed_text', '')
            cache_key = f"{text_key}_{item.get('type', '')}"
            self.cache[cache_key] = item.get('translated_text', '')
    
    def _show_performance_stats(self, total_items: int, cached_items: int, translated_items: int):
        """显示性能统计"""
        cache_hit_rate = (cached_items / total_items * 100) if total_items > 0 else 0
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("总项目数", total_items)
        
        with col2:
            st.metric("缓存命中", cached_items)
        
        with col3:
            st.metric("新翻译", translated_items)
        
        with col4:
            st.metric("缓存命中率", f"{cache_hit_rate:.1f}%")
        
        if cache_hit_rate > 50:
            st.success(f"🎉 缓存命中率 {cache_hit_rate:.1f}%，性能优化效果显著！")
        elif cache_hit_rate > 20:
            st.info(f"📈 缓存命中率 {cache_hit_rate:.1f}%，性能有所提升")
        else:
            st.warning(f"⚠️ 缓存命中率 {cache_hit_rate:.1f}%，建议增加缓存内容")

class FastTranslator:
    """快速翻译器 - 简化版翻译逻辑"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        import openai
        openai.api_key = api_key
    
    def _translate_paragraph_simple(self, text: str, target_lang: str) -> str:
        """简化的段落翻译"""
        try:
            import openai
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"Translate the following text to {target_lang}. Keep technical terms, proper nouns, and special names unchanged."},
                    {"role": "user", "content": text}
                ],
                max_tokens=500,
                temperature=0.1
            )
            return response.choices[0].message.content
        except Exception as e:
            return text
    
    def _translate_table_cell_simple(self, text: str, target_lang: str) -> str:
        """简化的表格单元格翻译"""
        return self._translate_paragraph_simple(text, target_lang)
