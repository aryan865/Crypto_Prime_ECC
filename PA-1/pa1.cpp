// nth_prime_bottom_formula.cpp
// Compile: g++ -O2 nth_prime_bottom_formula.cpp -o nthprime
// Run: ./nthprime

#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll rosser_upper_bound(ll n)
{
    if (n < 6)
        return 15;
    long double dn = (long double)n;
    long double ub = dn * (log(dn) + log(log(dn)));
    return (ll)ceil(ub);
}

// Sieve of Eratosthenes; returns vector isPrime[0..limit]
vector<char> sieve(ll limit)
{
    vector<char> isPrime(limit + 1, true);
    if (limit >= 0)
        isPrime[0] = false;
    if (limit >= 1)
        isPrime[1] = false;
    ll r = floor(sqrt((long double)limit));
    for (ll p = 2; p <= r; ++p)
    {
        if (isPrime[p])
        {
            for (ll q = p * p; q <= limit; q += p)
                isPrime[q] = false;
        }
    }
    return isPrime;
}

ll nth_prime_bottom_formula(ll n)
{
    if (n <= 0)
        return -1;
    const ll small[] = {2, 3, 5, 7, 11};
    if (n <= 5)
        return small[n - 1];

    ll upper = rosser_upper_bound(n);
    // add a small safety margin (rarely necessary)
    upper += 10;

    // compute primes up to upper
    vector<char> isP = sieve(upper);

    // prefix: pi[i] = number of primes <= i
    vector<ll> pi(upper + 1, 0);
    ll cnt = 0;
    for (ll i = 0; i <= upper; ++i)
    {
        if (isP[i])
            ++cnt;
        pi[i] = cnt;
    }

    // Evaluate formula: result = 1 + sum_{i=1..upper} floor( ( n / (pi(i)+1) )^(1/n) )
    // Use long double for pow
    long long result = 1; // the '1 +' in many formula variants
    for (ll i = 1; i <= upper; ++i)
    {
        long double denom = (long double)(pi[i] + 1);
        long double base = (long double)n / denom;
        // base may be <1 => pow <1 => floor = 0; otherwise >=1 => floor >=1 (usually 1)
        if (base < 1.0L)
            continue;
        // compute nth root:
        long double v = pow(base, 1.0L / (long double)n);
        ll term = (ll)floor(v + 1e-16L); // small eps to be safe
        result += term;
    }

    return result;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cout << "Enter n to find nth prime: ";
    if (!(cin >> n))
        return 0;
    if (n <= 0)
    {
        cout << "n must be positive\n";
        return 0;
    }
    long long p = nth_prime_bottom_formula(n);
    cout << n << "th prime (bottom-formula) = " << p << '\n';
    return 0;
}
