# Tool definitions for 556678.com. Each tool: slug, title, icon, short, fields, body (explainer HTML), faq.
TOOLS = [
 {"slug":"break-even","title":"Break-Even Calculator","icon":"⚖️","cat":"Profit",
  "short":"Find the exact number of sales you need each month before you make a single dollar of profit.",
  "fields":[("fixed","Monthly fixed costs ($)",6000),("price","Price per unit ($)",80),("variable","Variable cost per unit ($)",32),("target","Monthly profit target ($)",4000)],
  "body":"""<h2>How the break-even point works</h2>
<p>Every sale you make does two jobs. First it pays back the variable cost of that sale — the materials, packaging, shipping or payment fee that only exists because you sold something. Whatever is left over is the <strong>contribution margin</strong>, and that is the money that chips away at your fixed costs: rent, salaries, software, insurance. The break-even point is the moment the pile of contribution margins equals the pile of fixed costs.</p>
<p>The formula is simple: <em>break-even units = fixed costs ÷ (price − variable cost per unit)</em>. If your fixed costs are $6,000 a month, you sell at $80 and each unit costs $32 to deliver, each sale contributes $48 and you need 125 sales to cover the month.</p>
<h2>Three levers that move it</h2>
<ul><li><strong>Raise price.</strong> A 10% price increase often cuts the break-even point by far more than 10%, because the whole increase lands in contribution margin.</li>
<li><strong>Cut variable cost.</strong> Negotiating suppliers, bundling shipping or switching payment processors changes every single future sale.</li>
<li><strong>Trim fixed cost.</strong> The slowest lever, but it lowers the bar permanently.</li></ul>
<p>Use the profit-target field to see how many sales you need to pay yourself — break-even is the floor, not the goal.</p>""",
  "faq":[("Is break-even calculated monthly or yearly?","Either works as long as fixed costs and the sales period match. Monthly is the most useful for planning because it lines up with rent and payroll."),
         ("What if I sell many products?","Use a weighted average price and variable cost across your product mix, or run the calculator once per product line.")]},
 {"slug":"profit-margin","title":"Profit Margin & Markup Calculator","icon":"📈","cat":"Profit",
  "short":"Convert cost and price into gross margin and markup — and see the price needed for 50% or 70% margins.",
  "fields":[("cost","Cost per item ($)",24),("price","Selling price ($)",59)],
  "body":"""<h2>Margin and markup are not the same number</h2>
<p>Markup is profit measured against <em>cost</em>. Margin is profit measured against <em>price</em>. An item that costs $50 and sells for $100 has a 100% markup but a 50% margin. Confusing the two is one of the most common pricing mistakes: owners who "add 50%" to cost end up with a 33% margin and wonder where the money went.</p>
<h2>What is a healthy margin?</h2>
<p>It depends on the model. Software and digital products often run gross margins above 70%. Service businesses commonly land between 40% and 60% once labour is counted as cost. Retail and food typically sit lower, which is why volume and inventory turns matter so much in those sectors. Compare yourself to your own business model, not to someone else's.</p>
<div class="callout">Rule of thumb: if your gross margin cannot cover your fixed costs at realistic volume, no amount of marketing will fix it. Fix price or cost first.</div>""",
  "faq":[("How do I turn a target margin into a price?","Price = cost ÷ (1 − target margin). For a 60% margin on a $20 cost: 20 ÷ 0.4 = $50."),
         ("Should shipping be included in cost?","Yes, if you pay it. Anything you spend only because a sale happened belongs in cost of goods.")]},
 {"slug":"cash-runway","title":"Cash Runway & Burn Calculator","icon":"⏳","cat":"Cash flow",
  "short":"See how many months your cash lasts, with month-by-month projections that include revenue growth.",
  "fields":[("cash","Cash in the bank ($)",50000),("revenue","Monthly revenue today ($)",8000),("expenses","Monthly expenses ($)",14000),("growth","Monthly revenue growth (%)",5)],
  "body":"""<h2>Why runway is the number that matters most</h2>
<p>Profit is an opinion; cash is a fact. A business can show a profit on paper and still fail because customers pay late, inventory ties up money, or a loan payment lands before the revenue does. Cash-flow problems are widely reported as the leading factor in small-business closures, which is why this calculator sits at the centre of our toolkit.</p>
<p><strong>Net burn</strong> is how much more you spend than you take in each month. <strong>Runway</strong> is cash divided by burn — the number of months before the account hits zero. Adding a growth rate shows whether rising revenue closes the gap in time.</p>
<h2>How to extend runway fast</h2>
<ol><li>Invoice on delivery, not at month-end, and offer a small discount for early payment.</li>
<li>Move annual software subscriptions to monthly until revenue is stable.</li>
<li>Pre-sell: deposits, retainers and annual plans pull cash forward.</li>
<li>Open a credit line <em>before</em> you need it — lenders prefer borrowers who are not desperate.</li></ol>""",
  "faq":[("How much runway should I keep?","Many advisers suggest at least 6 months of operating expenses, and 12+ months if you are raising investment or in a seasonal industry."),
         ("Does this include taxes?","Include expected tax payments in monthly expenses for an accurate result.")]},
 {"slug":"loan-payment","title":"Business Loan Payment Calculator","icon":"🏦","cat":"Funding",
  "short":"Estimate monthly payments, total interest and yearly balance for a term loan or equipment financing.",
  "fields":[("amount","Loan amount ($)",75000),("apr","Annual interest rate (%)",11),("term","Term (months)",60)],
  "body":"""<h2>Reading a loan offer like a lender</h2>
<p>The monthly payment is only the start. Look at the <strong>total interest</strong> — the real price of the money — and the <strong>annual debt service</strong>, which lenders compare with your yearly operating cash flow. Most conventional lenders want to see cash flow of at least 1.25 times annual debt service before they are comfortable.</p>
<h2>Watch out for</h2>
<ul><li><strong>Factor rates</strong> quoted on short-term or merchant cash advances. A 1.3 factor on a 6-month advance can equal an APR well above 50%.</li>
<li><strong>Origination and packaging fees</strong> that are deducted from the amount you receive.</li>
<li><strong>Prepayment penalties</strong> that remove the benefit of paying early.</li></ul>
<p>Always compare offers on APR and total cost, not on the monthly payment alone.</p>""",
  "faq":[("Is this the exact payment I'll get?","It is an estimate based on a standard amortizing loan. Your lender's fees, rate type and payment schedule may differ."),
         ("What is a good APR for a small business loan?","It varies widely with credit, collateral, time in business and lender type. Government-backed programs and banks are usually cheaper than online short-term lenders.")]},
 {"slug":"pricing","title":"Product Pricing Calculator","icon":"🏷️","cat":"Profit",
  "short":"Work backwards from cost, payment fees and target margin to the minimum price you should charge.",
  "fields":[("cost","Unit cost incl. shipping ($)",18),("margin","Target profit margin (%)",40),("fees","Payment / marketplace fees (%)",3.5),("fixedfee","Fixed fee per order ($)",0.30)],
  "body":"""<h2>Price from the bottom up, then sanity-check from the top down</h2>
<p>This calculator gives you the <em>floor</em>: the lowest price that still delivers your target margin after percentage fees (card processing, marketplace commission) and fixed per-order fees. Below that price, every sale quietly erodes the business.</p>
<p>Then check the ceiling: what do customers compare you with, and what result do they get? Value-based pricing — anchoring to the outcome rather than your cost — is how small businesses escape the race to the bottom.</p>
<h2>Pricing moves that usually work</h2>
<ul><li>Offer three tiers. The middle tier tends to be chosen most often and lifts average order value.</li>
<li>Bundle complementary items rather than discounting single items.</li>
<li>Review prices at least once a year; costs rise even when you don't notice.</li></ul>""",
  "faq":[("What is charm pricing?","Ending prices in .99 or .95. It can lift conversion for consumer products; premium brands often prefer round numbers."),
         ("Should I include my own labour?","Yes. If you don't price your time, you are subsidising customers with unpaid work.")]},
 {"slug":"revenue-growth","title":"Revenue Growth & CAGR Calculator","icon":"🚀","cat":"Growth",
  "short":"Measure compound annual growth, doubling time and a forward projection at the same pace.",
  "fields":[("start","Starting revenue ($)",120000),("end","Current revenue ($)",260000),("years","Years between",3),("projyears","Projection horizon (years)",5)],
  "body":"""<h2>Why CAGR beats "we grew 117%"</h2>
<p>Total growth hides time. Growing 117% in three years is very different from 117% in one. The compound annual growth rate (CAGR) smooths the journey into one yearly rate, so you can compare periods, products and competitors fairly.</p>
<p><em>CAGR = (ending value ÷ starting value)^(1 ÷ years) − 1.</em> Doubling time uses the same rate: divide the natural log of 2 by the natural log of (1 + CAGR). The "rule of 72" — 72 divided by the growth percentage — is a handy mental shortcut.</p>
<h2>Use projections carefully</h2>
<p>Projecting the same CAGR forward is a scenario, not a forecast. Growth usually slows as a business gets bigger. Run a conservative and an aggressive case and plan cash for the conservative one.</p>""",
  "faq":[("Can CAGR be negative?","Yes — if revenue fell over the period, CAGR shows the average yearly rate of decline."),
         ("Is CAGR good for monthly data?","Use months as the period and you get a compound monthly growth rate instead.")]},
 {"slug":"startup-cost","title":"Startup Cost Calculator","icon":"🧮","cat":"Launch",
  "short":"Add up one-time launch costs plus an operating reserve to get a realistic launch budget.",
  "fields":[("legal","Registration, licences & legal ($)",1200),("equipment","Equipment & tools ($)",4000),("inventory","Opening inventory ($)",3000),("website","Website, branding & software ($)",1500),("marketing","Launch marketing ($)",2500),("deposits","Deposits & insurance ($)",1800),("other","Other one-time costs ($)",800),("monthly","Monthly operating costs ($)",4500),("buffer","Months of reserve",6)],
  "body":"""<h2>Most launch budgets forget the reserve</h2>
<p>Founders are good at listing what they need to <em>open</em> and bad at budgeting for the months <em>after</em> opening, when costs are running but customers are still discovering you. That gap is where many first-year failures happen. U.S. Bureau of Labor Statistics data has long shown that roughly one in five new businesses does not reach its second year.</p>
<p>This calculator combines one-time costs with a reserve measured in months of operating expenses. Six months is a sensible minimum for most service businesses; product, retail and hospitality concepts often need more.</p>
<h2>Where to find the money</h2>
<p>Personal savings remain the most common source of startup capital, followed by friends-and-family money, credit, microloans and grants. See our <a href="../guides/funding-options.html">funding options guide</a> for the trade-offs of each.</p>""",
  "faq":[("Should I count my own salary?","If you need to draw a salary to live, include it in monthly operating costs — otherwise your reserve is too small."),
         ("What are commonly forgotten costs?","Insurance deposits, payment-terminal hardware, professional fees, sales tax registration and the cost of your own time.")]},
 {"slug":"ai-roi","title":"AI ROI Calculator for Small Business","icon":"🤖","cat":"AI",
  "short":"Estimate what AI assistants and automations are really worth in hours and dollars for your team.",
  "fields":[("hours","Hours saved per person per week",4),("rate","Loaded hourly cost ($)",35),("people","People using it",3),("toolcost","Tool cost per person per month ($)",25),("setup","One-time setup / training cost ($)",600)],
  "body":"""<h2>Value AI by time returned, not by hype</h2>
<p>For most small businesses, the first real return from AI is time: drafting emails and proposals, summarising documents, answering routine customer questions, cleaning spreadsheets and producing first drafts of marketing content. The question is simple — how many hours a week does it give back, and what is an hour worth?</p>
<p>Use a <strong>loaded hourly cost</strong>: wages plus payroll taxes and benefits, or for owners, the rate you would bill a client. Be conservative about hours saved; measure for two weeks before and after adoption if you can.</p>
<h2>Where small teams see results first</h2>
<ul><li>Customer support triage and FAQ answers, with a human approving edge cases.</li>
<li>Bookkeeping categorisation and invoice follow-ups.</li>
<li>Content repurposing: one long article into posts, emails and scripts.</li>
<li>Sales prep: research summaries before calls.</li></ul>
<div class="callout">Time saved only becomes money if it is redeployed — into selling, serving more customers, or not hiring before you have to.</div>""",
  "faq":[("Is free AI good enough?","Free tiers are fine for trials. Paid plans usually add privacy controls, higher limits and team features that matter for business data."),
         ("What about risks?","Keep a human reviewing anything customer-facing, avoid pasting sensitive personal data into tools without a clear data policy, and check facts.")]},
 {"slug":"ltv-cac","title":"LTV : CAC Unit Economics Calculator","icon":"🔁","cat":"Growth",
  "short":"Check whether each customer is worth more than it costs to acquire — before you scale ad spend.",
  "fields":[("arpu","Average revenue per customer / month ($)",49),("gm","Gross margin (%)",75),("churn","Monthly churn (%)",4),("cac","Customer acquisition cost ($)",220)],
  "body":"""<h2>The ratio that decides whether growth is healthy</h2>
<p><strong>Lifetime value (LTV)</strong> is the gross profit a customer generates before they leave. <strong>Customer acquisition cost (CAC)</strong> is everything you spend in sales and marketing divided by the customers it produced. A ratio of about 3:1 is a widely used benchmark for subscription businesses: enough margin to fund growth without starving the company.</p>
<p>Equally important is <strong>CAC payback</strong> — how many months of gross profit it takes to earn back the acquisition cost. Short payback means growth funds itself; long payback means growth consumes cash.</p>
<h2>Improving the ratio</h2>
<ul><li>Reduce churn with better onboarding — retention compounds LTV faster than price increases.</li>
<li>Raise ARPU with annual plans, add-ons and tiered pricing.</li>
<li>Lower CAC with referrals, partnerships, SEO and content that keeps working after you publish it.</li></ul>""",
  "faq":[("Does this work for non-subscription businesses?","Yes. Use average monthly gross profit per active customer and the share of customers who stop buying each month."),
         ("Why use gross margin and not revenue?","Revenue overstates value; the cost of serving the customer has to come out first.")]},
 {"slug":"freelance-rate","title":"Freelance & Consulting Rate Calculator","icon":"💼","cat":"Launch",
  "short":"Turn your income goal, expenses, taxes and real billable hours into a minimum hourly rate.",
  "fields":[("income","Take-home income goal / year ($)",80000),("expenses","Business expenses / year ($)",9000),("tax","Effective tax rate (%)",25),("hours","Billable hours per week",25),("weeks","Working weeks per year",46)],
  "body":"""<h2>Billable hours are fewer than you think</h2>
<p>A 40-hour week rarely means 40 billable hours. Sales calls, admin, invoicing, learning and unpaid revisions eat into the week. Many independent professionals bill 20–30 hours in a typical week, and vacation, holidays and sick days remove several weeks a year.</p>
<p>This calculator starts with what you want to take home, adds business expenses, grosses up for tax and divides by realistic billable hours. The result is your <em>minimum</em> viable rate — not your market rate.</p>
<h2>Move from hours to outcomes</h2>
<p>Once you know your floor, package your work: fixed-price projects, retainers and productised services let you capture the value you create rather than the time you spend.</p>""",
  "faq":[("Should I publish my hourly rate?","Many consultants publish project starting prices instead, which anchors on value and avoids hourly comparisons."),
         ("How often should I raise rates?","Review at least yearly and whenever your calendar is consistently full.")]},
]
