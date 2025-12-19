"""
Unit-тесты для модуля битонной сортировки (Bitonic Sort)

Для запуска тестов используйте команду:
    python -m unittest test_sort.py
или
    python test_sort.py
"""

import unittest
from main import bitonic_sort, bitonic_merge, compare_and_swap


class TestBitonicSort(unittest.TestCase):
    """Класс для тестирования функции bitonic_sort"""
    
    def test_basic_sort(self):
        """Тест базовой сортировки"""
        arr = [12, 11, 13, 5, 6, 7, 8, 4]
        expected = [4, 5, 6, 7, 8, 11, 12, 13]
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_already_sorted(self):
        """Тест сортировки уже отсортированного массива"""
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_reverse_sorted(self):
        """Тест сортировки массива, отсортированного в обратном порядке"""
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_empty_array(self):
        """Тест сортировки пустого массива"""
        arr = []
        expected = []
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_single_element(self):
        """Тест сортировки массива с одним элементом"""
        arr = [42]
        expected = [42]
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_duplicates(self):
        """Тест сортировки массива с повторяющимися элементами"""
        arr = [3, 3, 3, 3]
        expected = [3, 3, 3, 3]
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_mixed_duplicates(self):
        """Тест сортировки массива со смешанными повторяющимися элементами"""
        arr = [5, 2, 8, 2, 9, 5, 1]
        expected = [1, 2, 2, 5, 5, 8, 9]
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Тест сортировки массива с отрицательными числами"""
        arr = [-5, -2, -8, 1, 9, -3]
        expected = [-8, -5, -3, -2, 1, 9]
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_power_of_two_size(self):
        """Тест сортировки массива размером степени двойки"""
        arr = [8, 3, 1, 6, 2, 7, 4, 5]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_non_power_of_two_size(self):
        """Тест сортировки массива размером не степень двойки"""
        arr = [5, 2, 8, 1, 9]
        expected = [1, 2, 5, 8, 9]
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_large_array_power_of_two(self):
        """Тест сортировки большого массива (степень двойки)"""
        arr = list(range(64, 0, -1))
        expected = list(range(1, 65))
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_large_array_non_power_of_two(self):
        """Тест сортировки большого массива (не степень двойки)"""
        arr = list(range(100, 0, -1))
        expected = list(range(1, 101))
        result = bitonic_sort(arr.copy())
        self.assertEqual(result, expected)
    
    def test_in_place_modification(self):
        """Тест, что функция изменяет исходный массив in-place"""
        arr = [3, 1, 4, 1, 5]
        original_id = id(arr)
        result = bitonic_sort(arr)
        # Проверяем, что это тот же объект
        self.assertEqual(id(result), original_id)
        # Проверяем, что массив отсортирован
        self.assertEqual(result, [1, 1, 3, 4, 5])
    
    def test_example_from_main(self):
        """Тест примеров из основного файла"""
        test_cases = [
            [64, 34, 25, 12, 22, 11, 90, 50],
            [5, 2, 8, 1, 9],
            [1],
            [3, 3, 3, 3],
            []
        ]
        
        for test in test_cases:
            with self.subTest(test=test):
                result = bitonic_sort(test.copy())
                expected = sorted(test)
                self.assertEqual(result, expected)


class TestCompareAndSwap(unittest.TestCase):
    """Класс для тестирования функции compare_and_swap"""
    
    def test_compare_swap_ascending(self):
        """Тест compare_and_swap для сортировки по возрастанию"""
        arr = [5, 3]
        compare_and_swap(arr, 0, 1, True)  # direction = True (по возрастанию)
        # 5 > 3, поэтому элементы должны поменяться местами
        self.assertEqual(arr, [3, 5])
    
    def test_compare_swap_descending(self):
        """Тест compare_and_swap для сортировки по убыванию"""
        arr = [3, 5]
        compare_and_swap(arr, 0, 1, False)  # direction = False (по убыванию)
        # 3 < 5, поэтому элементы должны поменяться местами
        self.assertEqual(arr, [5, 3])
    
    def test_compare_swap_no_swap_needed_ascending(self):
        """Тест compare_and_swap когда обмен не нужен (по возрастанию)"""
        arr = [3, 5]
        compare_and_swap(arr, 0, 1, True)  # direction = True
        # 3 < 5, обмен не нужен
        self.assertEqual(arr, [3, 5])
    
    def test_compare_swap_no_swap_needed_descending(self):
        """Тест compare_and_swap когда обмен не нужен (по убыванию)"""
        arr = [5, 3]
        compare_and_swap(arr, 0, 1, False)  # direction = False
        # 5 > 3, обмен не нужен
        self.assertEqual(arr, [5, 3])


class TestBitonicMerge(unittest.TestCase):
    """Класс для тестирования функции bitonic_merge"""
    
    def test_bitonic_merge_small_sequence(self):
        """Тест слияния маленькой битонной последовательности"""
        # Битонная последовательность: [3, 1] (убывает)
        arr = [3, 1]
        bitonic_merge(arr, 0, 2, True)  # Сливаем по возрастанию
        self.assertEqual(arr, [1, 3])
    
    def test_bitonic_merge_larger_sequence(self):
        """Тест слияния большей битонной последовательности"""
        # Битонная последовательность: [3, 4, 7, 8, 6, 5, 2, 1]
        # Сначала возрастает до 8, затем убывает
        arr = [3, 4, 7, 8, 6, 5, 2, 1]
        bitonic_merge(arr, 0, 8, True)  # Сливаем по возрастанию
        expected = sorted(arr)
        self.assertEqual(arr, expected)


if __name__ == "__main__":
    # Запуск тестов
    unittest.main(verbosity=2)

