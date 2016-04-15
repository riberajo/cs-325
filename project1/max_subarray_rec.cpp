#include <iostream>
#include <algorithm>
#include <time.h>

using namespace std;

int max_sub_array(int* array, int left_bound, int right_bound) {
  int left_max, mid_max, right_max, sub_max, total_sum = 0;
  int max_left_side = -1000000, max_right_side = -1000000;

  //Check if the is only one variable left
  if (left_bound == right_bound)
    return array[left_bound];

  //Find the maximum subarrays on the left and right
  left_max = max_sub_array(array,left_bound,(left_bound+right_bound)/2);
  right_max = max_sub_array(array,(left_bound+right_bound)/2+1,right_bound);

  //Maximum for a middle sub array array
  //Find max on left side
  for (int i = (left_bound+right_bound)/2; i >= left_bound; i--) {
    total_sum += array[i];
    //Update the left side maximum
    if (total_sum > max_left_side)
      max_left_side = total_sum;
  }
  total_sum = 0;
  //Find max on right side
  for (int i = (left_bound+right_bound)/2+1; i <= right_bound; i++) {
    total_sum += array[i];
    //Update the right side maximum
    if (total_sum > max_right_side)
      max_right_side = total_sum;
  }

  mid_max = max_left_side + max_right_side;

  //Finds the biggest of the three and returns it
  sub_max = max(max(left_max,right_max),mid_max);

  return sub_max;
}

int main() {
  int max;
  int array[] = {1, -5, 2, 6, -3, 0, -8, 9, 1};
  int bound = sizeof(array)/sizeof(int)-1;

  max = max_sub_array(array,0,bound);

  cout << "Max sub array: " << max << endl;

  return 0;
}
