#  Павел Попов, 7-я когорта, финальный проект. Автоматизация теста к API.
import sender_stand_request


def test_success_get_order_by_track():
    actual_status_code = sender_stand_request.get_order_by_track().status_code
    expected_status_code = 200
    assert actual_status_code == expected_status_code