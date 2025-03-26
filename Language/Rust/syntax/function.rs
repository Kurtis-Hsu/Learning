// 函数

fn main()
{
    println!("Hello world!");

    another_function(10);

    // Rust 中的块可以有返回值
    let x =
    {
        let y = 10;
        y + 1 // 注意这里没有分号，表示这是一个表达式，而非语句
    };
    println!("x = {x}");

    let x = add(1, 1);
    println!("x = {x}");
}

fn another_function(x: i32)
{
    println!("Another function.");

    println!("x = {x}");
}

fn add(x: i32, y: i32) -> i32
{
    x + y
    // 也可以使用 return 关键字返回值
    // return x + y;
}
