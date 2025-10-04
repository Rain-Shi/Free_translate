"""
测试AI智能识别特殊名称功能
"""

from smart_translator import SemanticTranslator
import json

def test_ai_special_name_identification():
    """测试AI智能识别特殊名称功能"""
    print("🧪 测试AI智能识别特殊名称功能")
    print("=" * 60)
    
    # 模拟API密钥（实际使用时需要真实密钥）
    api_key = "test-key"
    
    # 创建翻译器
    translator = SemanticTranslator(api_key)
    
    # 测试文本，包含各种特殊名称
    test_cases = [
        {
            "text": "The naiveHobo/InvoiceNet library is used for invoice processing.",
            "expected": ["naiveHobo/InvoiceNet"],
            "description": "GitHub库名识别"
        },
        {
            "text": "We use microsoft/TypeScript and facebook/react for development.",
            "expected": ["microsoft/TypeScript", "facebook/react"],
            "description": "多个GitHub库名识别"
        },
        {
            "text": "The project uses TensorFlow, PyTorch, and Scikit-learn for machine learning.",
            "expected": ["TensorFlow", "PyTorch", "Scikit-learn"],
            "description": "机器学习框架识别"
        },
        {
            "text": "OpenAI developed ChatGPT and GitHub Copilot for AI assistance.",
            "expected": ["OpenAI", "ChatGPT", "GitHub Copilot"],
            "description": "AI产品名称识别"
        },
        {
            "text": "The API uses HTTP, JSON, and OAuth for authentication.",
            "expected": ["HTTP", "JSON", "OAuth"],
            "description": "协议和标准识别"
        },
        {
            "text": "Python and JavaScript are popular programming languages.",
            "expected": ["Python", "JavaScript"],
            "description": "编程语言识别"
        },
        {
            "text": "Google, Microsoft, and Amazon are tech giants.",
            "expected": ["Google", "Microsoft", "Amazon"],
            "description": "公司名称识别"
        }
    ]
    
    print("📝 测试用例:")
    for i, case in enumerate(test_cases, 1):
        print(f"{i}. {case['description']}: {case['text']}")
    
    print("\n🔍 AI识别结果:")
    for i, case in enumerate(test_cases, 1):
        print(f"\n{i}. {case['description']}")
        print(f"原文: {case['text']}")
        
        try:
            # 使用AI识别特殊名称
            identified_names = translator._identify_special_names_with_ai(case['text'])
            print(f"AI识别结果: {identified_names}")
            
            # 检查识别准确性
            correct_identifications = [name for name in identified_names if name in case['text']]
            print(f"正确识别: {correct_identifications}")
            
            # 检查是否遗漏了期望的名称
            missed_names = [name for name in case['expected'] if name not in identified_names]
            if missed_names:
                print(f"遗漏的名称: {missed_names}")
            
            print("-" * 50)
            
        except Exception as e:
            print(f"❌ 识别失败: {str(e)}")
    
    print("\n✅ AI智能识别功能测试完成！")

def test_ai_protection_workflow():
    """测试AI保护工作流程"""
    print("\n🧪 测试AI保护工作流程")
    print("=" * 60)
    
    api_key = "test-key"
    translator = SemanticTranslator(api_key)
    
    test_text = "The naiveHobo/InvoiceNet library processes invoices using TensorFlow and PyTorch."
    
    print(f"测试文本: {test_text}")
    
    try:
        # 使用AI保护特殊名称
        protected_text, noun_mapping = translator._protect_special_names_with_ai(test_text)
        
        print(f"保护后文本: {protected_text}")
        print(f"映射表: {noun_mapping}")
        
        # 模拟翻译后的文本
        translated_text = "naiveHobo/InvoiceNet 库使用 TensorFlow 和 PyTorch 处理发票。"
        
        # 恢复特殊名称
        restored_text = translator._restore_proper_nouns(translated_text, noun_mapping)
        
        print(f"恢复后文本: {restored_text}")
        
        print("\n✅ AI保护工作流程测试完成！")
        
    except Exception as e:
        print(f"❌ 工作流程测试失败: {str(e)}")

def test_combined_protection():
    """测试组合保护（AI + 传统）"""
    print("\n🧪 测试组合保护功能")
    print("=" * 60)
    
    api_key = "test-key"
    translator = SemanticTranslator(api_key)
    
    test_text = "GitHub hosts naiveHobo/InvoiceNet, which uses Python and TensorFlow."
    
    print(f"测试文本: {test_text}")
    
    try:
        # AI智能保护
        protected_text, ai_mapping = translator._protect_special_names_with_ai(test_text)
        print(f"AI保护后: {protected_text}")
        print(f"AI映射: {ai_mapping}")
        
        # 传统专有名词保护
        protected_text, traditional_mapping = translator._protect_proper_nouns(protected_text)
        print(f"传统保护后: {protected_text}")
        print(f"传统映射: {traditional_mapping}")
        
        # 合并映射
        combined_mapping = {**ai_mapping, **traditional_mapping}
        print(f"合并映射: {combined_mapping}")
        
        print("\n✅ 组合保护功能测试完成！")
        
    except Exception as e:
        print(f"❌ 组合保护测试失败: {str(e)}")

def main():
    """主测试函数"""
    print("🚀 AI智能识别特殊名称功能测试")
    print("=" * 80)
    
    try:
        # 测试AI识别功能
        test_ai_special_name_identification()
        
        # 测试AI保护工作流程
        test_ai_protection_workflow()
        
        # 测试组合保护
        test_combined_protection()
        
        print("\n🎉 所有测试完成！")
        print("\n💡 注意：实际使用时需要有效的OpenAI API密钥")
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")

if __name__ == "__main__":
    main()
