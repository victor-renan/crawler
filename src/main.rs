use std::fs::read_to_string;
use std::error::Error;

const URLS_DIR: &str = "./urls.txt";
const OUT_DIR: &str = "./out";

fn main() -> Result<(), Box<dyn Error>> {
    for url in read_to_string(URLS_DIR).unwrap().lines() {
        // let html = reqwest::blocking::get(url)?.text();
        println!("{:?}", url);
    }

    Ok(())
}