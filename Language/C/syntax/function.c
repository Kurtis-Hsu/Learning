// 函数

#include <stdio.h>
int fun(int a); // 声明函数原型，参数名称声明可选

int /* 函数返回值类型 */ fun /* 函数名称/函数签名 */ (int a /* 参数 */)
{
    // 函数体

    return a; // 返回值，如果不声明返回值，默认返回0
}

void fun2(); // 无返回值函数

// 形参和实参
// 形参：函数定义时的参数，形参只有在函数内部有效
// 实参：函数调用时传递的参数，实参只有在函数调用时有效
int param(int a, int b) // 形参 a 和 b
{
    return a + b;
}

int main() // 主函数，c 程序必须从 main 函数开始执行
{
    // 调用函数
    printf("%d\n", fun(10));

    // 花括号表示一个代码块，代码块内部的变量只在代码块内部有效
    {
        int a = 10;
        printf("%d\n", a);
    }

    // printf("%d",a); // error: 'a' undeclared (first use in this function)

    printf("\n");
    printf("=== 形参和实参 ===\n");
    printf("%d\n", param(1, 2)); // 这里的 1 和 2 为实参

    return 0;
}

void fun2()
{
    printf("无返回值函数\n");
}
