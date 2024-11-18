"""
 datatype sample test
"""

import unittest
import asyncio
from hello_python.advance import asyncs_sample


class TestAsyncsSample(unittest.TestCase):
    """
    TestAsyncsSample
    """

    def test_once_async_sample(self):
        """
        test once async sample
        """
        asyncio.run(asyncs_sample.once_main())

    def test_task_async_sample(self):
        """
        test task async sample
        """
        asyncio.run(asyncs_sample.task_main())

    def test_scheduler_async_sample(self):
        """
        test Scheduler Asyncs task sample
        """
        asyncs_sample.schedule_main()

    def test_thread_task_sample(self):
        """
        test  ThreadPool Async task sample
        """
        asyncs_sample.thread_main()
