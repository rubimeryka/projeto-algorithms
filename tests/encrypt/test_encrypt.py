import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message("Hello World", "key")

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(1, 2)

    assert encrypt_message("Hello World", 3) == "Hell_odl_lroW"
    assert encrypt_message("Hello World", 6) == "Wro_llodl_eH"
    assert encrypt_message("OpenAI", 5) == "AI_neO"
    assert encrypt_message("", 0) == ""
    assert encrypt_message("abc", 1) == "abc"