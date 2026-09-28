import unittest

from man import TaskStore


class TaskStoreTest(unittest.TestCase):
    def test_add_task_stores_non_empty_task(self):
        store = TaskStore()

        self.assertTrue(store.add("Pay bills"))
        self.assertEqual(store.tasks, ["Pay bills"])

    def test_add_task_rejects_empty_input(self):
        store = TaskStore()

        self.assertFalse(store.add(""))
        self.assertEqual(store.tasks, [])

    def test_delete_selection_removes_first_selected_task(self):
        store = TaskStore(["first", "second", "third"])

        self.assertEqual(store.delete_selection((1,)), 1)
        self.assertEqual(store.tasks, ["first", "third"])

    def test_delete_selection_handles_no_selection(self):
        store = TaskStore(["first"])

        self.assertIsNone(store.delete_selection(()))
        self.assertEqual(store.tasks, ["first"])

    def test_delete_selection_handles_out_of_range_selection(self):
        store = TaskStore(["first"])

        self.assertIsNone(store.delete_selection((3,)))
        self.assertEqual(store.tasks, ["first"])
