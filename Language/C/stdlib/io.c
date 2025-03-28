// IO

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
// stdio.h 包含了用于控制台输入输出的 printf 和 scanf 函数
// scanf 函数用于接收用户输入的信息，返回字符串类型
// printf 函数用于输出信息到控制台
// scanf 已被标记为不安全，使用 scanf 会出现警告，推荐使用 scanf_s 替代 scanf

int main()
{
    int var = 1;

    printf("=== 格式化符号 ===\n");
    printf("size：%zd", sizeof(long double));
    printf("整数：%d\n", 10);
    printf("无符号整数：%u\n", 10);
    printf("浮点数：%f\n", 3.14);
    printf("字符：%c\n", 'a');
    printf("字符串：%s\n", "hello");
    printf("十六进制：%x\n", 10);
    printf("八进制：%o\n", 10);
    printf("科学计数法：%e\n", 3.14e-2);
    printf("指数：%g\n", 3.14e2);
    printf("指针：%p\n", &var);

    // 断行
    printf("Here's a long \
string\n");
    printf(
        "Here's a long "
        "string\n"
    );

    printf("\n=== 控制台 IO ===\n");

    char name[10];
    int age;
    printf("输入姓名，年龄：");
    scanf("%s %d", &name, &age);
    printf("姓名：%s 年龄：%d\n", name, age);
}
