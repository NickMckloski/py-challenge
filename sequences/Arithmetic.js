/**
 * Creates a new expression
 * @param variable - {character} the variable used in the expression, given as single character
 * @param expression - {string} expression with the variable, uses standard math operators
 * @constructor
 */
function Expression(variable, expression) {
    this.variable = variable;
    this.string = expression;
}

/**
 * Creates a sequence from an expression and a start+end point
 * @param expression - {expression} the expression to take
 * @param start - {number} start point
 * @param end - {number} end point
 * @param step - {number} the step, or amount to skip by
 * @constructor
 */
function Sequence(expression, start, end, step) {
    this.expression = expression;
    this.start = start;
    this.end = end;
    this.step = step;

    /**
     * Returns the string formatted output of the sequence
     * @returns {string}
     */
    this.print = function() {
        var sequence = "";
        for(var i = start; i <= end; i += step) {
            var stringExpression = expression.string.replace(expression.variable, i);
            var output = eval(stringExpression);
            sequence += output + (i + step <= end ? '+' : '');
        }
        return sequence;
    }

    /**
     * Returns the nth term in a sequence
     * @param n - {number} the nth term
     * @returns {number}
     */
    this.nthTerm = function(n) {
        var firstTerm = eval(expression.string.replace(expression.variable, start));
        var secondTerm = eval(expression.string.replace(expression.variable, start + 1));
        var difference = Math.abs(firstTerm-secondTerm);
        var nth = firstTerm + difference * (n - 1);
        return nth;
    }

    /**
     * Returns the sum of the sequence
     * @returns {Object}
     */
    this.sum = function() {
        return eval(this.print());
    }

}

/**
 * Tests
 */
var exp = new Expression('n', '-3+3*n');
var seq = new Sequence(exp, 0, 5, 2);

console.log(seq.print());
console.log(seq.nthTerm(3));
console.log(seq.sum());

