- [Identify rrors and orrection results](#identify-rrors-and-orrection-results)
  - [1](#anchor-1)
  - [2](#anchor-2)


# Identify rrors and orrection results

## 1

 Error related to new lief. It happends when running pestudio with `indicators` function

 ![image](images/README/screenshot_23-06-2023_19h50m32.png)

  Correction: Change method `has_signature` to `has_signatures`. Here is the result:

 ![image](images/README/screenshot_23-06-2023_20h11m19.png)

## 2

Errors: This error is also mentioned in Pestudio project - Header Issues and the author also suggested solutions: Change line 1146: machine --> machine.value. or use old version of LIEF library. Here we use the first suggested solution.

![image](images/README/screenshot_23-06-2023_19h29m13.png)

![image](images/README/screenshot_23-06-2023_18h40m12.png)

Correction results:

![image](images/readme/screenshot_01-07-2023_11h53m05.png)

![image](images/readme/screenshot_01-07-2023_12h11m36.png)

![image](images/README/screenshot_23-06-2023_18h41m49.png)

![image](images/README/screenshot_23-06-2023_18h42m43.png)
