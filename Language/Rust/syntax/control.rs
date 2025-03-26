// 控制流程

fn main()
{
    // if 表达式
    let number = 3;

    if number < 5 { println!("number < 5"); }
    else if number == 5 { println!("number == 5"); }
    else { println!("number > 5"); }

    // Rust 中的 if 是一个表达式，可以使用在 let 语句中
    let condition = true;
    let number = if condition { 5 } else { 6 };
    println!("number = {number}");

    // loop 循环
    let mut counter = 0usize;

    let n = 'lebal:  loop // 使用 'lebal: 可以给 loop 循环命名
    {
        counter += 1;

        if counter == 3 { continue; } // 使用 continue 跳过本次循环

        println!("loop {counter}");

        if counter == 5 { break counter * 2; } // 使用 break 退出循环，循环可以带返回值

        if counter == 4 { break 'lebal 1; } // 使用 break 'lebal; 或 continue 'lebal; 跳出或继续指定的循环

        // break 仅是退出当前循环，使用 return 退出整个函数
    };
    println!("n = {n}");

    // while 循环
    let mut number = 3;

    while number != 0
    {
        println!("while {number}");

        number -= 1;
    }

    // for 循环
    let arr = [10, 20, 30, 40, 50];

    for e in arr
    {
        println!("for {e}");
    }

    for n in (1..4).rev()
    {
        println!("{n}!");
    }
}
