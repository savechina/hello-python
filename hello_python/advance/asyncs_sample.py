import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def fetch_data(task_id, delay):
    """模拟一个异步 I/O 操作，例如从网络获取数据。"""
    print(f"Task {task_id} started, will take {delay} seconds.")
    await asyncio.sleep(delay)  # 模拟 I/O 操作的延迟
    print(f"Task {task_id} completed.")
    return f"Data from task {task_id}"


async def once_main():
    # 创建多个异步任务
    tasks = [fetch_data(1, 2), fetch_data(2, 3), fetch_data(3, 1)]

    # 并发运行所有任务，并等待它们完成
    results = await asyncio.gather(*tasks)

    # 打印所有任务的返回结果
    for result in results:
        print(result)


async def task_main():
    # 创建多个异步任务
    tasks = [
        asyncio.create_task(fetch_data(1, 2)),
        asyncio.create_task(fetch_data(2, 4)),
        asyncio.create_task(fetch_data(3, 1)),
    ]

    try:
        # 设置一个超时时间，假设我们希望所有任务在3秒内完成
        results = await asyncio.wait_for(asyncio.gather(*tasks), timeout=3)
    except asyncio.TimeoutError:
        print("Some tasks took too long and were cancelled.")

    # 处理任务结果
    for task in tasks:
        if not task.cancelled():
            try:
                result = task.result()
                print(f"Task result: {result}")
            except Exception as e:
                print(f"Task raised an exception: {e}")


async def my_async_task():
    print("Task started")
    await asyncio.sleep(2)  # Simulate an I/O-bound operation
    print("Task completed")


async def my_async_task_with_timeout(timeout):
    try:
        await asyncio.wait_for(my_async_task(), timeout)
    except asyncio.TimeoutError:
        print("Task timed out")


async def schedule_delay_down(scheduler):
    await asyncio.sleep(20)
    scheduler.shutdown(True)


def schedule_main():
    # Create an instance of AsyncIOScheduler
    scheduler = AsyncIOScheduler()

    # Add the asynchronous job with timeout to the scheduler
    scheduler.add_job(
        my_async_task_with_timeout, "interval", seconds=5, args=(1,)
    )  # 1 second timeout

    # Start the scheduler
    scheduler.start()

    try:
        # run the asyncio event loop utils complete
        asyncio.get_event_loop().run_until_complete(schedule_delay_down(scheduler))

        # Run the asyncio event loop
        # asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass


async def cpu_bound_task():
    # 模拟 CPU 密集型任务
    sum = 0
    for i in range(10000000):
        # print("i")
        sum = sum + i
    print("CPU task finished,sum:", sum)


async def io_bound_task():
    # 模拟 I/O 密集型任务
    await asyncio.sleep(1)
    print("I/O task finished")


async def thread_pool_task():
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_running_loop()
        future = loop.run_in_executor(executor, cpu_bound_task)
        # future = cpu_bound_task
        await io_bound_task()
        await future.result()


def thread_main():
    asyncio.run(thread_pool_task())
