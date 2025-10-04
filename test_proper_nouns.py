"""
测试专有名词保护功能
"""

from smart_translator import SemanticTranslator
import json

def test_proper_noun_protection():
    """测试专有名词保护功能"""
    print("🧪 测试专有名词保护功能")
    print("=" * 50)
    
    # 模拟API密钥（实际使用时需要真实密钥）
    api_key = "test-key"
    
    # 创建翻译器
    translator = SemanticTranslator(api_key)
    
    # 测试文本
    test_texts = [
        "GitHub is a popular code hosting platform.",
        "OpenAI developed ChatGPT and GPT models.",
        "Python is a powerful programming language.",
        "Streamlit makes it easy to create web apps.",
        "Microsoft and Google are tech giants.",
        "The HTTP protocol is widely used.",
        "JavaScript and TypeScript are popular languages."
    ]
    
    print("📝 测试文本:")
    for i, text in enumerate(test_texts, 1):
        print(f"{i}. {text}")
    
    print("\n🔍 专有名词检测:")
    for text in test_texts:
        protected_text, noun_mapping = translator._protect_proper_nouns(text)
        if noun_mapping:
            print(f"原文: {text}")
            print(f"保护后: {protected_text}")
            print(f"检测到的专有名词: {list(noun_mapping.values())}")
            print("-" * 30)
    
    print("\n✅ 专有名词保护功能测试完成！")

def test_custom_proper_nouns():
    """测试自定义专有名词"""
    print("\n🧪 测试自定义专有名词功能")
    print("=" * 50)
    
    api_key = "test-key"
    translator = SemanticTranslator(api_key)
    
    # 添加自定义专有名词
    custom_nouns = ["MyCompany", "MyProduct", "MyAPI", "MyService"]
    translator.add_proper_nouns(custom_nouns)
    
    test_text = "MyCompany developed MyProduct using MyAPI and MyService."
    
    print(f"测试文本: {test_text}")
    
    protected_text, noun_mapping = translator._protect_proper_nouns(test_text)
    
    print(f"保护后: {protected_text}")
    print(f"检测到的专有名词: {list(noun_mapping.values())}")
    
    print("\n✅ 自定义专有名词功能测试完成！")

def test_proper_noun_restoration():
    """测试专有名词恢复功能"""
    print("\n🧪 测试专有名词恢复功能")
    print("=" * 50)
    
    api_key = "test-key"
    translator = SemanticTranslator(api_key)
    
    original_text = "GitHub and OpenAI are great platforms."
    
    # 保护专有名词
    protected_text, noun_mapping = translator._protect_proper_nouns(original_text)
    print(f"原文: {original_text}")
    print(f"保护后: {protected_text}")
    print(f"映射表: {noun_mapping}")
    
    # 模拟翻译后的文本（专有名词被替换为占位符）
    translated_text = "GitHub 和 OpenAI 是很好的平台。"
    
    # 恢复专有名词
    restored_text = translator._restore_proper_nouns(translated_text, noun_mapping)
    print(f"恢复后: {restored_text}")
    
    print("\n✅ 专有名词恢复功能测试完成！")

def main():
    """主测试函数"""
    print("🚀 专有名词保护功能测试")
    print("=" * 60)
    
    try:
        # 测试基本功能
        test_proper_noun_protection()
        
        # 测试自定义专有名词
        test_custom_proper_nouns()
        
        # 测试恢复功能
        test_proper_noun_restoration()
        
        print("\n🎉 所有测试完成！")
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")

if __name__ == "__main__":
    main()
