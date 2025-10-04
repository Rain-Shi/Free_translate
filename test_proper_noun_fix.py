"""
测试专有名词保护修复
"""

from smart_translator import SemanticTranslator

def test_proper_noun_protection():
    """测试专有名词保护功能"""
    print("🧪 测试专有名词保护修复")
    print("=" * 50)
    
    # 创建翻译器
    api_key = "test-key"
    translator = SemanticTranslator(api_key)
    
    # 添加测试专有名词
    test_nouns = [
        "ielke/ai-financial-report-agents",
        "jennifer sequina/financial_reports_automation", 
        "GitHub",
        "OpenAI",
        "Python"
    ]
    translator.add_proper_nouns(test_nouns)
    
    # 测试文本
    test_cases = [
        {
            "text": "ielke/ai-financial-report-agents",
            "expected": "ielke/ai-financial-report-agents"
        },
        {
            "text": "jennifer sequina/financial_reports_automation",
            "expected": "jennifer sequina/financial_reports_automation"
        },
        {
            "text": "GitHub is a popular platform",
            "expected": "GitHub is a popular platform"
        },
        {
            "text": "OpenAI developed ChatGPT",
            "expected": "OpenAI developed ChatGPT"
        }
    ]
    
    print("📝 测试用例:")
    for i, case in enumerate(test_cases, 1):
        print(f"{i}. 原文: {case['text']}")
        
        # 保护专有名词
        protected_text, noun_mapping = translator._protect_proper_nouns(case['text'])
        print(f"   保护后: {protected_text}")
        print(f"   映射表: {noun_mapping}")
        
        # 恢复专有名词
        restored_text = translator._restore_proper_nouns(protected_text, noun_mapping)
        print(f"   恢复后: {restored_text}")
        
        # 检查是否正确
        if restored_text == case['expected']:
            print("   ✅ 正确")
        else:
            print("   ❌ 错误")
        
        print("-" * 30)
    
    print("\n✅ 专有名词保护测试完成！")

def test_duplicate_protection():
    """测试重复保护问题"""
    print("\n🧪 测试重复保护问题")
    print("=" * 50)
    
    api_key = "test-key"
    translator = SemanticTranslator(api_key)
    
    # 添加可能重复的专有名词
    test_nouns = [
        "ielke/ai-",
        "ielke/ai-financial-report-agents",
        "GitHub",
        "OpenAI"
    ]
    translator.add_proper_nouns(test_nouns)
    
    test_text = "ielke/ai-financial-report-agents is a GitHub project"
    
    print(f"测试文本: {test_text}")
    
    # 保护专有名词
    protected_text, noun_mapping = translator._protect_proper_nouns(test_text)
    print(f"保护后: {protected_text}")
    print(f"映射表: {noun_mapping}")
    
    # 恢复专有名词
    restored_text = translator._restore_proper_nouns(protected_text, noun_mapping)
    print(f"恢复后: {restored_text}")
    
    # 检查是否出现重复
    if "ielke/ai-ielke/ai-" in restored_text:
        print("❌ 发现重复前缀问题")
    else:
        print("✅ 没有重复前缀问题")
    
    print("\n✅ 重复保护测试完成！")

def main():
    """主测试函数"""
    print("🚀 专有名词保护修复测试")
    print("=" * 80)
    
    try:
        # 测试基本保护功能
        test_proper_noun_protection()
        
        # 测试重复保护问题
        test_duplicate_protection()
        
        print("\n🎉 所有测试完成！")
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")

if __name__ == "__main__":
    main()
