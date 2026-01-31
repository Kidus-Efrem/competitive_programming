public class Solution {
    public bool CanMakeArithmeticProgression(int[] arr) {
        Array.Sort(arr);
        Console.Write(String.Join(" ",arr ));
        int change = arr[1]- arr[0];
        for (int i = 2; i < arr.Length; i++){
            if ( arr[i] - arr[i-1] != change){
                return false;
            }
        }
        return true;
    }
}