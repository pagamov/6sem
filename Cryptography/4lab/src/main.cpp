#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

size_t clever_mod(const int64_t &a, const size_t &p) {
    int64_t res = a % int64_t(p);
    return res >= 0 ? res : p + res;
}

size_t gcd(const size_t& a, const size_t& b) {
    return b ? gcd(b, a % b) : a;
}

int64_t gcd(const int64_t &a, const size_t &b, int64_t &x, int64_t &y) {
    if (a == 0) {
        x = 0; y = 1;
        return b;
    }
    int64_t x1, y1;
    gcd(b % a, a, x1, y1);
    x = y1 - (b / a) * x1;
    y = x1;
    return x;
}

size_t rev(const int64_t& a, const size_t& b) {
    if (a == b)
        throw "bad!";
    int64_t x, y;
    gcd(a, b, x, y);
    return clever_mod(x, b);
}

size_t sqr(const size_t& n) {
    if (n == 0)
        return 0;
    size_t x = n;
    size_t prev = x;
    while (true) {
        x = (x + n / x) / 2;
        if (prev == x || (x + n / x) / 2 == x + 1)
            break;
        else
            prev = x;
    }
    return x;
}

struct EL {
    int64_t a;
    int64_t b;
    size_t p;

    EL(const int64_t& a_in, const int64_t& b_in, const size_t& p_in) {
        a = a_in;
        b = b_in;
        p = p_in;
    }
    size_t find(vector <pair <size_t, size_t>> &vec) const {
        if ((4 * a * a * a + 27 * b * b) % p == 0)
            return 0;
        int64_t y_get;
        size_t y;
        size_t count = 0;
        for (size_t x = 0; x < p; x++) {
            y_get = clever_mod((x * x * x + a * x + b), p);
            for (y = sqr(y_get); y < p; y++)
                if ((y * y) % p == y_get) {
                    if (!count) {
                        vec.push_back({ x, y });
                    }
                    // cout << "new: " << x << ' ' << y << " all: " << vec.size() << endl;
                    count++;
                }
        }
        return count + 1;
    }
};

struct EL_point {
    size_t x;
    size_t y;
    EL* el;
    EL_point(const size_t &x_in, const size_t &y_in, EL* ptr) {
        x = x_in;
        y = y_in;
        el = ptr;
    }
    EL_point operator-() const {
        return { x, el->p - y, el };
    }
    EL_point operator=(const EL_point& p) {
        x = p.x;
        y = p.y;
        el = p.el;
        return *this;
    }
    bool operator==(const EL_point& point) const {
        if (x != point.x || y != point.y)
            return false;
        return true;
    }
    // bool operator!=(const EL_point& p) const {
    //     if (*this == p)
    //         return false;
    //     return true;
    // }
    EL_point operator+(const EL_point& point) const {
        if (*this == -point)
            return {0, 0, el};
        else if (*this == point) {
            size_t m;
            size_t x_new;
            m = clever_mod(clever_mod((3 * x * x) % el->p + el->a, el->p)*rev((2 * y) % el->p, el->p), el->p);
            x_new = clever_mod((m * m) % el->p - (2 * x) % el->p, el->p);
            return { x_new, clever_mod((m * clever_mod(x - x_new, el->p)) % el->p - y, el->p), el };
        }
        size_t m;
        size_t x_new;
        m = clever_mod(clever_mod(point.y - y, el->p)*rev(clever_mod(point.x - x, el->p), el->p), el->p);
        x_new = clever_mod((m * m) % el->p - x - point.x, el->p);
        return { x_new, clever_mod((m * clever_mod(x - x_new, el->p)) % el->p - y, el->p), el };
    }
};

int main() {
    // EL e(502, 31, 307969);
    EL e(1488, 228, 9181);
    size_t order;
    vector <pair <size_t, size_t>> points;

    size_t count = 1;
    EL_point p(0, 0, nullptr);
    EL_point s(0, 0, nullptr);

    clock_t start = clock();
    order = e.find(points);
    cout << "order: " << order << endl;

    size_t min = order;
    for (size_t i = 0; i < points.size(); i++) {
        p = EL_point(points[i].first, points[i].second, &e);
        s = p;
        while (s.y) {
            s = s + p;
            count++;
        }
        if (count < min)
            min = count;
            if (min == 1)
                break;
        count = 1;
    }
    cout << "order point: " << min << endl;
    cout << "lose time: " << float(clock() - start) / CLOCKS_PER_SEC << endl;
    return 0;
}
