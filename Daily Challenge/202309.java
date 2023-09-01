class Solution {
	// 20230901: Counting Bits https://leetcode.com/problems/counting-bits/
	public int[] countBits(int n) {
		int[] ans = new int[n + 1];
		for (int i = 0; i <= n; i++) {
			ans[i] = -1;
		}

		for (int i = 0; i <= n; i++) {
			int count = 0;
			int currentNumber = i;

			count += currentNumber & 1;

			while (currentNumber != 0) {
				currentNumber >>= 1;
				if (ans[currentNumber] != -1) {
					count += ans[currentNumber];
					break;
				} else {
					count += currentNumber & 1;
				}
			}

			ans[i] = count;
		}

		return ans;
	}

	public static void main(String args[]) {
		Solution s = new Solution();
		int[] ans = s.countBits(5);
		for (int i = 0; i < ans.length; i++) {
			System.out.println(ans[i]);
		}
	}
}