from src.frame import Frame


def test_frame_validation():
    data = "9-"
    frame = Frame(data)
    assert frame.validate_pins()
