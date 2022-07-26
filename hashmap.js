class Bucket {
    constructor() {
        this.bucket = []
    }
    get(key) {
        for(let [k, v] of this.bucket) {
            if (k === key) {
                return v
            }
            return -1
        }
    }
    update(key, value) {
        let found = false
        this.bucket.forEach((kv, i) => {
            if (key === kv[0]) {
                this.bucket[i] = [key, value]
                found = true
                return
            }
        })
        if (!found) {
            this.bucket.push([key, value])
        }
    }
    remove(key) {
        this.bucket.forEach((kv, i) => {
            if (key === kv[0]) {
                this.bucket.splice(i, 1)
            }
        })
    }
}
class MyHashMap {
    constructor() {
        this.keySpace = 2069
        this.hashMap = []
        for (let i = 0; i < this.keySpace; i++) {
            this.hashMap.push(new Bucket())
        }
    }
    put(key, value) {
        const hashKey = key % this.keySpace
        this.hashMap[hashKey].update(key, value)
    }
    get(key) {
        const hashKey = key % this.keySpace
        return this.hashKey[hashKey].get(key)
    }
    remove(key) {
        const hashKey = key % this.keySpace
        return this.hashMap[hashKey].remove(key)
    }
}

/** 
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
