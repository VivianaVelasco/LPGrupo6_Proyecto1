List<int> moveZeroes(List<int> nums) {
  int lastNonZeroFoundAt = 0;

  for (int i = 0; i < nums.length; ++i) {
    if (nums[i] != 0) {
      nums[lastNonZeroFoundAt] = nums[i];
      lastNonZeroFoundAt += 1;
    }
  }

  for (int i = lastNonZeroFoundAt; i < nums.length; ++i) {
    nums[i] = 0;
  }
  return nums;
  // Comentarios
  /*    OTRO coMENTARIO       */
}