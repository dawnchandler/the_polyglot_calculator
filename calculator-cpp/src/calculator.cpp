/**
 * Compute the sum an array
 * @param n number of elements
 * @param array input array
 * @return sum
 */

#include <ctime>
#include <cmath>
using namespace std;

extern "C"
float* add(float x, float y) {
    const clock_t begin_time = clock();
    float result = x + y;
    float execution_milliseconds = float( clock () - begin_time ) /  CLOCKS_PER_SEC;
    float* vals = new float[2];
    vals[0] = result;
    vals[1] = execution_milliseconds;
    return vals;
}

extern "C"
float* sub(float x, float y) {
    const clock_t begin_time = clock();
    float result = x - y;
    float execution_milliseconds = float( clock () - begin_time ) /  CLOCKS_PER_SEC;
    float* vals = new float[2];
    vals[0] = result;
    vals[1] = execution_milliseconds;
    return vals;
}

extern "C"
float* mult(float x, float y) {
    const clock_t begin_time = clock();
    float result = x * y;
    float execution_milliseconds = float( clock () - begin_time ) /  CLOCKS_PER_SEC;
    float* vals = new float[2];
    vals[0] = result;
    vals[1] = execution_milliseconds;
    return vals;
}

extern "C"
float* divide(float x, float y) {
    const clock_t begin_time = clock();
    float result = x / y;
    float execution_milliseconds = float( clock () - begin_time ) /  CLOCKS_PER_SEC;
    float* vals = new float[2];
    vals[0] = result;
    vals[1] = execution_milliseconds;
    return vals;
}

extern "C"
float* power(float x, float y) {
    const clock_t begin_time = clock();
    float result = pow(x, y);
    float execution_milliseconds = float( clock () - begin_time ) /  CLOCKS_PER_SEC;
    float* vals = new float[2];
    vals[0] = result;
    vals[1] = execution_milliseconds;
    return vals;
}