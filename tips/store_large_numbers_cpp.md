
## Food for thought 

Πόσο μεγάλους αριθμούς θα μπορούσαμε να γράψουμε σε ένα πρόγραμμα της c++;
Το μεγαλύτερο όριο κάποιου τύπου δίνεται από unsigned long long int (μεγάλους θετικούς ακεραίους)  

__ULLONG_MAX__	 
Maximum value for an object of type: 18446744073709551615 (2^64-1) *εξαρτάται από την υλοποίηση της βιβλιοθήκης στο κάθε σύστημα

Στις καθημερινές εφαρμογές που μπορεί να φτιάξουμε μπορεί 20 ψηφία να είναι αρκετά όμως ας φανταστούμε πόσα ψηφία θα χρειζόταν ένα ιδιωτικό κλειδί RSA 3072. 



### Prime Numbers Cooperative Computing 

Ακόμα και τα απλά μαθηματικά όταν εφαρμόζονται σε μεγάλους αριθμούς αποκταν ιδιαίτερη δυσκολία. Φανταστείτε το κόσκινο του Ερατοσθένη και σκεφτείτε μέσα στο άπειρο ποιος είναι ο μεγαλύτερος πρώτος αριθμός που μπορείτε να βρείτε.

Πριν τους υπολογιστές ο μεγαλύτερος πρώτος αριθμός που είχε βρεθει περιείχε 44 ψηφία και η μέθοδος ήταν το θεώρημα του Proth. Θα πιστεύαμε πως με έναν υπολογιστή θα μπορούσαμε συνεχώς να βρίσκουμε κάθε μέρα και μεγαλύτερους πρώτους αριθμούς.

Όμως υπολογιστικά κάτι τέτοιο χρειάζεται πάρα πολλούς πόρους καθώς και προηγμένες μαθηματικές και προγραμματιστικές τεχνικές. Πλεόν για κάθε νέο πρώτο αριθμό που ανακαλύπτεται υπάρχει χρηματικό έπαθλο (ξεκινάει από 3000 ως 250000 δολλάρια). Η υπολογιστική ισχύ που χρειάζεται είναι τόσο μεγάλη που από το 1997 έχει δημιουργηθεί το project GIMPS που χρησιμοποιεί την κατανεμημένη ισχύ υπολογιστών παγκοσμίως για την εύρεση νέων πρώτων αριθμών. 

Ο μεγαλύτερος πρώτος αριθμός που βρέθηκε τον Δεκέμβριο του 2018 έχει 24,862,048 ψηφία. 

### Μεγάλα Παραγοντικά

Όμως ένα πιο απτό προγραμματιστικό παράδειγμα είναι η εύρεση των παραγοντικών. Ακόμα και το παραγοντικό του 100! ≈ 9.33262×10^157
Πως θα μπορούσαμε να αναπαριστήσουμε αυτό τον αριθμό στην c++;


## Solve 1


```c++
// C++ program to compute factorial of big numbers 
#include<iostream> 
using namespace std; 
  
// Maximum number of digits in output 
#define MAX 500 
  
int multiply(int x, int res[], int res_size); 
  
// This function finds factorial of large numbers 
// and prints them 
void factorial(int n) 
{ 
    int res[MAX]; 
  
    // Initialize result 
    res[0] = 1; 
    int res_size = 1; 
  
    // Apply simple factorial formula n! = 1 * 2 * 3 * 4...*n 
    for (int x=2; x<=n; x++) 
        res_size = multiply(x, res, res_size); 
  
    cout << "Factorial of given number is \n"; 
    for (int i=res_size-1; i>=0; i--) 
        cout << res[i]; 
} 
  
// This function multiplies x with the number  
// represented by res[]. 
// res_size is size of res[] or number of digits in the  
// number represented by res[]. This function uses simple  
// school mathematics for multiplication. 
// This function may value of res_size and returns the  
// new value of res_size 
int multiply(int x, int res[], int res_size) 
{ 
    int carry = 0;  // Initialize carry 
  
    // One by one multiply n with individual digits of res[] 
    for (int i=0; i<res_size; i++) 
    { 
        int prod = res[i] * x + carry; 
  
        // Store last digit of 'prod' in res[]   
        res[i] = prod % 10;   
  
        // Put rest in carry 
        carry  = prod/10;     
    } 
  
    // Put carry in res and increase result size 
    while (carry) 
    { 
        res[res_size] = carry%10; 
        carry = carry/10; 
        res_size++; 
    } 
    return res_size; 
} 
  
// Driver program 
int main() 
{ 
    factorial(100); 
    return 0; 
} 

```

## Output 1

Factorial of given number is                                                                                            
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000         

## Solve 2


```c++
#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <iomanip>
#include <vector>


void print_factorials()
{
   using boost::multiprecision::cpp_int;
   //
   // Print all the factorials that will fit inside a 128-bit integer.
   //
   // Begin by building a big table of factorials, once we know just how 
   // large the largest is, we'll be able to "pretty format" the results.
   //
   // Calculate the largest number that will fit inside 128 bits, we could
   // also have used numeric_limits<int128_t>::max() for this value:
   cpp_int limit = (cpp_int(1) << 128) - 1;
   // 
   // Our table of values:
   std::vector<cpp_int> results;
   //
   // Initial values:
   unsigned i = 1;
   cpp_int factorial = 1;
   //
   // Cycle through the factorials till we reach the limit:
   while(factorial < limit)
   {
      results.push_back(factorial);
      ++i;
      factorial *= i;
   }
   //
   // Lets see how many digits the largest factorial was:
   unsigned digits = results.back().str().size();
   //
   // Now print them out, using right justification, while we're at it
   // we'll indicate the limit of each integer type, so begin by defining
   // the limits for 16, 32, 64 etc bit integers:
   cpp_int limits[] = {
      (cpp_int(1) << 16) - 1,
      (cpp_int(1) << 32) - 1,
      (cpp_int(1) << 64) - 1,
      (cpp_int(1) << 128) - 1,
   };
   std::string bit_counts[] = { "16", "32", "64", "128" };
   unsigned current_limit = 0;
   for(unsigned j = 0; j < results.size(); ++j)
   {
      if(limits[current_limit] < results[j])
      {
         std::string message = "Limit of " + bit_counts[current_limit] + " bit integers";
         std::cout << std::setfill('.') << std::setw(digits+1) << std::right << message << std::setfill(' ') << std::endl;
         ++current_limit;
      }
      std::cout << std::setw(digits + 1) << std::right << results[j] << std::endl;
   }
}
```

## Output 2

                                       1
                                       2
                                       6
                                      24
                                     120
                                     720
                                    5040
                                   40320
................Limit of 16 bit integers
                                  362880
                                 3628800
                                39916800
                               479001600
................Limit of 32 bit integers
                              6227020800
                             87178291200
                           1307674368000
                          20922789888000
                         355687428096000
                        6402373705728000
                      121645100408832000
                     2432902008176640000
................Limit of 64 bit integers
                    51090942171709440000
                  1124000727777607680000
                 25852016738884976640000
                620448401733239439360000
              15511210043330985984000000
             403291461126605635584000000
           10888869450418352160768000000
          304888344611713860501504000000
         8841761993739701954543616000000
       265252859812191058636308480000000
      8222838654177922817725562880000000
    263130836933693530167218012160000000
   8683317618811886495518194401280000000
 295232799039604140847618609643520000000


## Libraries

Φυσικά σε μια γλώσσα όπως η C++ υπάρχουν και οι αντίστοιχες βιβλιοθήκες που θα μπορούσαν να κάνουν τα παραπάνω αυτοματοποιημένα:

BigIntegerCPP
GMP
MAPM

#### Εξάσκηση

Πως θα μπορούσαμε αντίστοιχα να κάνουμε πρόσθεση δύο μεγάλων αριθμών;

## References

https://www.eff.org/awards/coop
https://www.mersenne.org/
https://www.geeksforgeeks.org/factorial-large-number/
http://www.cplusplus.com/reference/climits/
https://secure-media.collegeboard.org/apc/ap01.pdf.lr_7928.pdf
https://github.com/technophilis/BigIntegerCPP
https://gmplib.org/

