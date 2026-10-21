import pytest

from circular_queue import Queue, run_cmd_with_queue

def test_circular_wraparound_behavior():
    q = Queue(3)

    q.push(1)
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    assert q.pop() == 2

    # 앞에서 pop된 공간을 재사용(원형 큐)
    q.push(4)
    q.push(5)

    assert q.size() == 3
    assert q.front() == 3
    assert q.back() == 5

    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5
    assert q.pop() == -1


def test_run_cmd_with_queue_prints_expected_output(capsys):
    q = Queue(2)

    run_cmd_with_queue(q, ["push", "1"])
    run_cmd_with_queue(q, ["push", "2"])
    run_cmd_with_queue(q, ["push", "3"])  # full -> -1 출력
    run_cmd_with_queue(q, ["front"])       # 1
    run_cmd_with_queue(q, ["back"])        # 2
    run_cmd_with_queue(q, ["size"])        # 2
    run_cmd_with_queue(q, ["empty"])       # 0
    run_cmd_with_queue(q, ["pop"])         # 1
    run_cmd_with_queue(q, ["pop"])         # 2
    run_cmd_with_queue(q, ["pop"])         # -1

    out = capsys.readouterr().out.strip().splitlines()
    assert out == ["-1", "1", "2", "2", "0", "1", "2", "-1"]