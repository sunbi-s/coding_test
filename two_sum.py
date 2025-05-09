class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small = 0
        big = len(numbers) - 1

        while small < big:
            current_sum = numbers[small] + numbers[big]
            if current_sum == target:
                # index가 1부터 시작
                return [small + 1, big + 1]
            elif current_sum > target:
                big -= 1
            else:
                small += 1

        # 만약 정답이 없다면 (문제 조건이 아닐 경우엔 예외처리 고려)
        return []

