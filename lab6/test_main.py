from unittest import mock
from main import main

def test_main_function():
    """Test the main function logic using mock for print and parking logic."""
    with mock.patch('builtins.print') as mocked_print:
        main()

        assert mocked_print.call_count > 0

        print_args = [call[0][0].strip() for call in mocked_print.call_args_list]

        assert "Створюємо паркінг з максимальною кількістю 3 місця і ціною за годину 20 грн" in print_args
        assert "Паркуємо машини" in print_args
        assert "Автомобіль AA1234BB припарковано." in print_args
        assert "Спроба запаркувати 4 машину на переповнений паркінг" in print_args
        assert "Автомобіль залишає паркінг" in print_args
        assert "Сортуємо машини за тривалістю стоянки" in print_args
