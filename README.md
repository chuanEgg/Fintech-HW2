# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

> tokenB->tokenA->tokenD->tokenC->tokenB

> tokenB balance: 20.129888944077447

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

> Slippage is difference between your expected price and the actual price.

> For example, if the initial liquidity pool is 10 ETH and 30000 USDC, you call for the swap function at this exact moment to swap 3000 USDC into ETH. While your buy order is pending to be confirmed by the blockchain, someone swap 3000 USDC to get 0.919 ETH (ignore swap fee), changing the pool to 9.091 ETH and 33000 USDC. Now you only get 0.757 ETH, less than your original expectation. The price difference between 0.919 ETH and 0.757 ETH is the slippage.

> To cope with slippage, users can set a maximum slippage tolerance and a trading dealine.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

> The existence of minimum liquidity is to prevent the value of liquidity tokens to be easily manipulated. In the absence of minimum liquidity, one can own the entirity of the liquidity of a pool, and the said user can easily raise the value of his liquidity tokens by donating funds to the pool, to a point where it will be almost impossible for other users to provide liquidity (the minimum unit of liquidity pool share will be absurdly costly). If we burn some part of the liquidity pool tokens, the raise of value of liquidity pool shares will we diluted by the burnt ones, increasing the cost of price manipulation. 

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

> The liquidity shares returned to the minter is porpotional to the worse ratio of the tokens provided, this encourage the minter to provide liquidity without changing the ratio of the pool. This method is more fair for earlier liquid providers as well.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

> Attackers will place one order in front of your order (by providing more gas fee) and one after your order. The first order will increase the price of the token you are trying to buy and thus increase the slippage, essentially creating a artificial price increase. The second order sells the token you just bought with an increase price. You will have a higher slippage if you encountered a sandwich attack. For example, assume that you placed an order to buy 100 ETH with 300,000 USDC. The attacker will buy the ETH before you, slightly increase ETH's price to perhaps 3005 USDC, now you can only buy 99.83 ETH. After that, the attacker will sell the tokens back with the increased value (the price increased because you just bought them).

