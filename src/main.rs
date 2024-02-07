use std::fs::File;
use std::io::Read;
use std::error::Error;

const URLS_DIR: &str = "urls.txt";


fn main() -> Result<(), Box<dyn Error>> {
    let html = reqwest::blocking::get("https://www2.camara.leg.br/legin/fed/lei/2021/lei-14133-1-abril-2021-791222-publicacaooriginal-162591-pl.html")?.text();

    println!("{:?}", html);

    Ok(())
}

fn get_urls() -> Result<(), Box<dyn Error>> {
    let mut reader = File::open(URLS_DIR)?;
    let mut urls = vec![];

    reader.read_to_end(&mut urls)?;

    Ok(())
}