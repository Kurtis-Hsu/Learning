#![allow(dead_code)]

#[derive(Debug)]
struct User // 定义一个结构体
{
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

// 方法
impl User
{
    // 方法的第一个参数始终是 &self，指代调用该方法的结构体实例
    // &self 是 self: $Self 的缩写，使用时用 self
    fn say_hi(&self) { println!("Hello, i'm {}", self.username); }
    
    // Rust 中没有固定的构造函数语法，可以使用关联函数，比如 String::from
    fn new_user(username: String) -> Self
    {
        let email = format!("{}@mail.com", username.clone());
        Self
        {
            active: true,
            email,
            username,
            sign_in_count: 1,
        }
    }
}

// 元组结构
// 可以使用元组的形式创建一个结构体，元组结构只需要声明属性类型，而不需要属性名称
#[derive(Debug)]
struct Color(u8, u8, u8);

// 定义一个没有属性的结构体，称为单元结构体
struct Unit;

// 枚举类型
#[derive(Debug)]
enum IpAddrKind
{
    // 枚举可以实现类似定义有限构造函数的形式
    V4(u8, u8, u8, u8),
    V6(String),
}

fn main()
{
    // 创建一个结构体的实例
    let mut user = User
    {
        active: true,
        username: String::from("someone"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };

    dbg!(&user);
    user.email = String::from("another@exampl.com");
    dbg!(&user);
    
    let user = build_user(String::from("builded"), String::from("builded@example.com"));
    dbg!(&user);
    
    let new_user = User
    {
        username: String::from("another"),
        ..user // 该行必须放在最后
        // 以上面的 user 为基础创建一个新结构体实例
        // 除了指定的 username 外，其余的属性值都与 user 相同
    };
    dbg!(&new_user);
    dbg!(&user.username);
    // dbg!(&user.email); // 报错
    // 结构更新语法等同于变量移动，原结构体中的 email 属性不再有效

    let red = Color(255, 0, 0);
    dbg!(&red);
    // 解构元组结构
    let Color(r, g, b) = red;
    dbg!(&r, &g, &b);

    let tom = build_user(String::from("tom"), String::from("tom@mail.com"));
    tom.say_hi();

    let jack = User::new_user(String::from("jack"));
    jack.say_hi();

    let home = IpAddrKind::V4(127, 0, 0, 1);
    dbg!(home);
    let loopback = IpAddrKind::V6(String::from("::1"));
    dbg!(loopback);
}

fn build_user(username: String, email: String) -> User
{
    User
    {
        active: true,
        username, // 若字段名与某个变量名相同，可以简化
        email,
        sign_in_count: 1,
    }
}
