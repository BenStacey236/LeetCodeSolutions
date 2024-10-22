# Medium Problem
# Problem 238

def productExceptSelfNoDiv(nums: list[int]) -> list[int]:
    answers = [1] * len(nums)

    prefix = 1
    for i, num in enumerate(nums):
        answers[i] = prefix
        prefix *= num

    post = 1
    for i, num in enumerate(reversed(nums)):
        answers[len(answers)-i-1] *= post
        post *= num

    return answers


input = [1,2,3,4]

if __name__ == "__main__":
    print(productExceptSelfNoDiv(input))