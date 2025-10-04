"""
测试页面对比功能
"""

from smart_translator import StructuralParser, DualViewEditor
import streamlit as st

def test_page_detection():
    """测试页面检测功能"""
    print("🧪 测试页面检测功能")
    print("=" * 50)
    
    # 创建解析器
    parser = StructuralParser()
    
    # 模拟段落数据
    test_paragraphs = [
        {"text": "Title Page", "style": "Title"},
        {"text": "Chapter 1: Introduction", "style": "Heading 1"},
        {"text": "This is the first paragraph.", "style": "Normal"},
        {"text": "This is the second paragraph.", "style": "Normal"},
        {"text": "Chapter 2: Methods", "style": "Heading 1"},
        {"text": "This is the third paragraph.", "style": "Normal"},
        {"text": "This is the fourth paragraph.", "style": "Normal"},
        {"text": "Chapter 3: Results", "style": "Heading 1"},
        {"text": "This is the fifth paragraph.", "style": "Normal"},
    ]
    
    print("📄 段落页面检测结果:")
    for i, para in enumerate(test_paragraphs):
        # 模拟段落对象
        class MockParagraph:
            def __init__(self, text, style):
                self.text = text
                self.style = MockStyle(style)
        
        class MockStyle:
            def __init__(self, name):
                self.name = name
        
        mock_para = MockParagraph(para["text"], para["style"])
        page_num = parser._detect_page_number(mock_para, i)
        
        print(f"段落 {i+1}: '{para['text']}' -> 第 {page_num} 页")
    
    print("\n✅ 页面检测功能测试完成！")

def test_page_organization():
    """测试页面组织功能"""
    print("\n🧪 测试页面组织功能")
    print("=" * 50)
    
    # 创建编辑器
    editor = DualViewEditor()
    
    # 模拟内容项
    test_items = [
        {"text": "Title Page", "type": "paragraph", "layout": {"page_number": 1}},
        {"text": "Chapter 1", "type": "paragraph", "layout": {"page_number": 2}},
        {"text": "Content 1", "type": "paragraph", "layout": {"page_number": 2}},
        {"text": "Content 2", "type": "paragraph", "layout": {"page_number": 2}},
        {"text": "Chapter 2", "type": "paragraph", "layout": {"page_number": 3}},
        {"text": "Content 3", "type": "paragraph", "layout": {"page_number": 3}},
        {"text": "Table Cell 1", "type": "table_cell", "layout": {"page_number": 3}},
        {"text": "Table Cell 2", "type": "table_cell", "layout": {"page_number": 3}},
    ]
    
    # 按页面组织
    pages = editor._organize_by_pages(test_items)
    
    print("📄 页面组织结果:")
    for page_num, items in pages.items():
        print(f"第 {page_num} 页:")
        for item in items:
            print(f"  - {item['type']}: {item['text']}")
    
    print("\n✅ 页面组织功能测试完成！")

def test_page_stats():
    """测试页面统计功能"""
    print("\n🧪 测试页面统计功能")
    print("=" * 50)
    
    # 模拟页面数据
    original_items = [
        {"text": "Original paragraph 1", "type": "paragraph"},
        {"text": "Original paragraph 2", "type": "paragraph"},
        {"text": "Original table cell 1", "type": "table_cell", "table_index": 0},
        {"text": "Original table cell 2", "type": "table_cell", "table_index": 0},
    ]
    
    translated_items = [
        {"text": "翻译段落 1", "type": "paragraph", "translated_text": "翻译段落 1"},
        {"text": "翻译段落 2", "type": "paragraph", "translated_text": "翻译段落 2"},
        {"text": "翻译表格单元格 1", "type": "table_cell", "table_index": 0, "translated_text": "翻译表格单元格 1"},
        {"text": "翻译表格单元格 2", "type": "table_cell", "table_index": 0, "translated_text": "翻译表格单元格 2"},
    ]
    
    # 计算统计信息
    orig_para_count = len([item for item in original_items if item.get('type') == 'paragraph'])
    trans_para_count = len([item for item in translated_items if item.get('type') == 'paragraph'])
    
    orig_table_count = len(set(item.get('table_index', 0) for item in original_items if item.get('type') == 'table_cell'))
    trans_table_count = len(set(item.get('table_index', 0) for item in translated_items if item.get('type') == 'table_cell'))
    
    orig_chars = sum(len(item.get('text', '')) for item in original_items)
    trans_chars = sum(len(item.get('translated_text', item.get('text', ''))) for item in translated_items)
    
    print("📊 页面统计结果:")
    print(f"段落数: {orig_para_count} → {trans_para_count}")
    print(f"表格数: {orig_table_count} → {trans_table_count}")
    print(f"字符数: {orig_chars} → {trans_chars}")
    
    if orig_chars > 0:
        ratio = trans_chars / orig_chars
        print(f"长度比例: {ratio:.2f}")
    
    print("\n✅ 页面统计功能测试完成！")

def test_table_organization():
    """测试表格组织功能"""
    print("\n🧪 测试表格组织功能")
    print("=" * 50)
    
    # 模拟表格单元格数据
    table_cells = [
        {"text": "Header 1", "type": "table_cell", "table_index": 0, "row": 0, "col": 0},
        {"text": "Header 2", "type": "table_cell", "table_index": 0, "row": 0, "col": 1},
        {"text": "Data 1", "type": "table_cell", "table_index": 0, "row": 1, "col": 0},
        {"text": "Data 2", "type": "table_cell", "table_index": 0, "row": 1, "col": 1},
        {"text": "Header A", "type": "table_cell", "table_index": 1, "row": 0, "col": 0},
        {"text": "Header B", "type": "table_cell", "table_index": 1, "row": 0, "col": 1},
    ]
    
    # 按表格分组
    tables = {}
    for cell in table_cells:
        table_idx = cell.get('table_index', 0)
        if table_idx not in tables:
            tables[table_idx] = []
        tables[table_idx].append(cell)
    
    print("📊 表格组织结果:")
    for table_idx, cells in tables.items():
        print(f"表格 {table_idx + 1}:")
        for cell in cells:
            print(f"  [{cell['row']}][{cell['col']}]: {cell['text']}")
    
    print("\n✅ 表格组织功能测试完成！")

def main():
    """主测试函数"""
    print("🚀 页面对比功能测试")
    print("=" * 80)
    
    try:
        # 测试页面检测
        test_page_detection()
        
        # 测试页面组织
        test_page_organization()
        
        # 测试页面统计
        test_page_stats()
        
        # 测试表格组织
        test_table_organization()
        
        print("\n🎉 所有测试完成！")
        print("\n💡 页面对比功能已准备就绪！")
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")

if __name__ == "__main__":
    main()
