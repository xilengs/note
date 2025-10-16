import pytest
from survey import AnonymousSurvey

# 当测试函数的一个形参与应用了装饰器@pytest.fixture的函数(夹具)同名时
# 将自动运行夹具，并将夹具返回的值传递给测试函数
@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的 AnonymousSurvey 实例"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """测试单个答案是否会被妥善存储"""
    """
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    """

    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_response(language_survey):
    """测试三个答案是否会被妥善存储"""
    """
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    """

    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses