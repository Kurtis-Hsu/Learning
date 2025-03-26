// 注释

// Rust 只支持单行注释，不支持多行注释

/// Rust 也支持文档格式的注释，可以使用 `///` 或 `//!` 开头
///
/// 这种注释会被 rustdoc 工具提取，生成 markdown 格式的文档
fn main()
{
    println!("Hello world!");
}
