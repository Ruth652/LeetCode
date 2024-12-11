/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
if(x<0||x%10===0&&x!=0){
    return false;
}
    
    let num=x;
    let reverse=0;
    while(num>0){
        let d=num%10;
       reverse = reverse * 10 + d; 
        num = Math.trunc(num / 10); 
    }
    return x===reverse;
};