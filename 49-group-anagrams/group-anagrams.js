/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let obj={};
    for(let i=0;i<strs.length;i++){
        let uniqueArray = Array(26).fill(0);
        for(let j=0;j<strs[i].length;j++){
            let index= strs[i][j].charCodeAt()-'a'.charCodeAt();
            ++uniqueArray[index];
        }
        if(!obj[uniqueArray]){
            obj[uniqueArray] = [strs[i]];
        }else {
            obj[uniqueArray].push(strs[i]);
        }
    }
    return Object.values(obj);
};