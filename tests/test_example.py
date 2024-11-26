from hexlet_pytest.example import reverse

def test_reverse():
    #text_to_test_path = 'fixtures/text_to_test.txt'
    with open("tests/fixtures/text_for_test.txt", encoding='utf8') as f:
        text_to_test = f.read()

   # corr_answer_path = 'fixtures/corr_answer.txt'    
    with open("tests/fixtures/corr_answer.txt", encoding='utf8') as f1:
        corr_answer = f1.read()

    #assert reverse('Hexlet') == 'telxeH'
    assert reverse(text_to_test) == corr_answer


#def test_reverse_for_empty_string():
 #   assert reverse('') == ''
