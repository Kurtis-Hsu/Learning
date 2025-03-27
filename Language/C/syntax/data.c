// 数据

int var; // 声明变量，变量名为 var，类型为 int
// var = 10; // 赋值，将 10 赋值给 var，这个步骤必须在方法或块内部，不能在全局作用域内

// 变量名可以由字母、数字、下划线组成，不能以数字开头，区分大小写
// 变量名不能是关键字，关键字是编程语言保留的，有特殊含义的单词，例如 int、char、if、else 等
// c99 和 c11 根据 UCN（Universal Character Names）规范支持中文变量名
int 整数 = 10;

const int con = 10; // 不能被修改的变量称为常量，const 修饰的变量不能被修改

// 字面量
// 字面量是指程序中直接使用的数据，例如 10、3.14、'a'、"hello" 等
// 整型字面量默认为 int 类型，浮点型字面量默认为 double 类型
// 整型字面量：10、0x10、010、0b10
// 浮点型字面量：3.14、3.14f、3.14e-2、3.14e2
// 字符型字面量：'a'、'\n'、'\0'、'\\'、'\''、'\"'
// 字符串字面量："hello"、"hello\nworld"、"hello\"world"

// 二进制
int bin = 0b10; // 二进制字面量，0b 或 0B 开头
// 八进制
int oct = 010; // 八进制字面量，0 开头
// 十六进制
int hex = 0x10; // 十六进制字面量，0x 或 0X 开头

int var2 = 20;          // 声明变量的同时赋值，变量名为 var2，类型为 int，值为 20
int var3 = 1, var4 = 2; // 声明多个变量

// c 语言中的数据类型包含基本数据类型和构造数据类型
// 基本数据类型：整型、浮点型、字符型、枚举型、空类型
// 构造数据类型：数组、结构体、共用体、指针、函数
// 各数据类型占用字节根据编译器和操作系统的不同而不同

// 整型
// 整型用于存储整数，包括有符号整型和无符号整型
// 整型默认为有符号整型
signed int sn = 10;        // 有符号整型，signed 可被省略
int n1 = 10;                // 根据寄存器大小，一般为 4 字节
short n2 = 10;              // 2 ~ 4 字节
long n3 = 10;               // 4 ~ 8 字节
long long n4 = 10;          // 8 字节
unsigned int n5 = 10;       // 无符号整型
unsigned short n6 = 10;     // 无符号短整型
unsigned long n7 = 10;      // 无符号长整型
unsigned long long n8 = 10; // 无符号长长整型

// 可以直接使用编译器自带的固定长度整型
#include <stdint.h>
int8_t i1 = 10;   // 1 字节
int16_t i2 = 10;  // 2 字节
int32_t i3 = 10;  // 4 字节
int64_t i4 = 10;  // 8 字节
uint8_t i5 = 10;  // 1 字节 无符号整型
uint16_t i6 = 10; // 2 字节 无符号整型
uint32_t i7 = 10; // 4 字节 无符号整型
uint64_t i8 = 10; // 8 字节 无符号整型

int si = 10;    // 默认为有符号整型
int si1 = 10u;  // 后缀 u 表示无符号整型
int si2 = 10l;  // 后缀 l 表示长整型
int si3 = 10ul; // 后缀 ul 表示无符号长整型

// 浮点型
// 浮点型用于存储小数，包括单精度浮点型和双精度浮点型
float f = 3.14;  // 4 字节
double d = 3.14; // 8 字节
long double ld = 3.14;

float f1 = 3.14f;       // 后缀 f 表示单精度浮点型
double d1 = 3.14;       // 默认为双精度浮点型
long double d3 = 3.14L; // 后缀 L 表示长双精度浮点型

// 科学计数法
float f2 = 3.14e-2; // 3.14 * 10^-2
double d2 = 3.14e2; // 3.14 * 10^2

// 字符型
// 字符型用于存储字符，底层存储为整数
// 部分编译器 char 默认为有符号整型，部分编译器 char 默认为无符号整型
// c99 和 c11 标准规定 char 为有符号整型
// 可以使用 signed char、unsigned char 明确指定有符号或无符号
char c1 = 'a'; // 1 字节
char c2 = 97; // 97 对应的字符为 a
char c4 = '\n'; // 换行符
char c3 = '中'; // c99 和 c11 支持中文字符

// 布尔值
// C 语言没有内置的布尔类型，使用 1 和 0 代替，stdbool.h 头文件中定义了 bool、true、false
#include <stdbool.h>
bool b1 = true;
bool b2 = false;

#include <stdio.h>

int main()
{
    printf("%d\n", 整数);

    // 数值溢出
    int max = 2147483647;
    unsigned int umax = 4294967295;

    printf("\n");
    printf("=== 数值溢出 ===\n");
    printf("打印 int 2147483647：%d\n", max);
    printf("打印 int 2147483647 + 1：%d\n", max + 1);
    printf("打印无符号 int 4294967295：%u\n", umax);
    printf("打印无符号 int 4294967295 + 1：%u\n", umax + 1);

    printf("\n");
    printf("=== 格式化输出 ===\n");
    printf("整数：%d\n", 10);
    printf("无符号整数：%u\n", 10);
    printf("浮点数：%f\n", 3.14);
    printf("字符：%c\n", 'a');
    printf("字符串：%s\n", "hello");
    printf("十六进制：%x\n", 10);
    printf("八进制：%o\n", 10);
    printf("科学计数法：%e\n", 3.14e-2);
    printf("指数：%g\n", 3.14e2);
    printf("指针：%p\n", &f);

    return 0;
}
