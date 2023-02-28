# Pipeline
## Tech Stack
- `typescript` 
- `jest`

## Description
This poc is trying to create a pipeline pattern where we can chain multiple functions together and pass the result of one function to the next function. The pipeline is a function that takes a value and a list of functions and returns the result of the last function in the list. The pipeline function should be able to take any number of functions.

## Example
    
    
    const result = Pipe().A.B.C;
    const {result, error} = Pipe.run();
    
for this example, pipe  will run function A then pass the result to function B and then pass the result to function C. The result of function C will be returned.

Any error that occurs in any of the functions will be returned in the error property of the result object.