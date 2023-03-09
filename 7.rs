impl Solution {
    pub fn reverse(x: i32) -> i32 {
        if x < 0 {
            let xs: String = x.abs().to_string().chars().rev().collect();
            format!("-{}", xs)
        } else {
            x.to_string().chars().rev().collect()
        }.parse().unwrap_or(0)
    }
}
