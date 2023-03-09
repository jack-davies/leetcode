impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if haystack == needle {
            // catches edge case haystack == needle == ""
            return 0
        }

        let haystack_bytes = haystack.as_bytes();
        let needle_bytes = needle.as_bytes();

        for i in 0..haystack_bytes.len() {
            let mut found = true;
            for j in 0..needle_bytes.len() {
                if haystack_bytes.get(i+j) != needle_bytes.get(j) {
                    found = false;
                    break
                }
            }
            if found {
                return i as i32
            }
        }
        -1
    }
}
