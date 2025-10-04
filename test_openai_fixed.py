"""
测试修复后的OpenAI API连接
"""
import openai

def test_openai_connection(api_key):
    """测试OpenAI API连接"""
    try:
        # 设置API密钥
        openai.api_key = api_key
        
        # 使用兼容的调用方式
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Hello, please respond with 'API connection successful'"}
            ],
            max_tokens=50,
            temperature=0.3
        )
        
        result = response.choices[0].message.content
        print(f"OpenAI API测试成功: {result}")
        return True
        
    except Exception as e:
        print(f"OpenAI API测试失败: {e}")
        return False

if __name__ == "__main__":
    print("测试OpenAI API连接...")
    print("请确保您有有效的OpenAI API密钥")
    api_key = input("请输入您的OpenAI API密钥进行测试 (或按回车跳过): ")
    if api_key:
        test_openai_connection(api_key)
    else:
        print("跳过API测试")
