# Chef Bob reference recipes

104 recipe entries and variants, including incomplete recipe notes. Imported on **3 October 2026** from the maintainer's recipe collection, last modified **26 August 2026**.

All recipes below use a **5-portion base**. See [portions and scaling](#portions-and-scaling) to adjust them.

For a first plan, start with the six complete [starter recipes](recipes/STARTER_RECIPES.md). Use the index below to browse this larger collection. Ask Chef Bob to show a dish or category in plain language. The [command guide](COMMANDS.md) explains `/help`, `/plan`, `/preferences`, and `/recipe-add`.

## How to use this collection

- **Imported draft**: formatted source notes that may still lack amounts or cooking steps. Read **Notes** before planning; use another recipe or clarify any gap that affects cooking or the shopping list.
- **Adapted draft**: suggested quantities and completed steps have been added for practical use. Defaults, ranges and changes are explained in the entry. These recipes have been checked for consistency but have not been kitchen-tested.
- Source links and stable recipe IDs are retained. New amounts replace undefined measures where noted; they are not claims about what the original cook used. Some other entries still contain unresolved amounts, ingredient identities or cooking steps.
- Apply allergies, exclusions and substitutions when planning. Ingredients in the shared collection are independent of any household's preferences.
- `/recipe-add` saves additions privately. It does not publish them or edit this file. To share a recipe, follow the [contribution process](CONTRIBUTING.md).
- Preparation notes, archived entries and variants explicitly marked incomplete remain reference material, not planning defaults.

## Portions and scaling

Every recipe in this collection is based on **5 portions**. The listed ingredient quantities make the full five-portion batch. The maintainer confirmed this on 6 October 2026, replacing the earlier missing or conflicting serving notes.

To cook a different amount, multiply each specified ingredient quantity by **your portions / 5**.

| Portions wanted | Multiply listed quantities by |
| ---: | ---: |
| 1 | 0.2 |
| 2 | 0.4 |
| 3 | 0.6 |
| 4 | 0.8 |
| 5 | 1, use as written |
| 6 | 1.2 |
| 10 | 2 |

For example, 500 g of an ingredient becomes 200 g for 2 portions or 300 g for 3 portions. Each recipe's portion count refers to that dish; a side dish is still a side dish.

Follow recipe-specific scaling notes first. The [ginger soy fish sauce](#ginger-soy-baked-salmon), for example, should not be doubled automatically. Cooking times and temperatures do not scale with portions; check the batch size and method separately. Use the [quantity guide](#choosing-quantities) for defaults and ranges. Any remaining undefined measurements still need clarification.

You can ask Bob:

```text
Use RECIPES.md to plan dinners for 3 portions. Its recipes are based on
5 portions, so scale the listed quantities by 0.6. Follow any recipe-specific
scaling notes, apply my food preferences, and flag missing measurements.
```

## Choosing quantities

In an adapted recipe, the **first amount is the default** and the following range is optional. All amounts refer to the full **5-portion batch**. These are suggested cooking amounts added on 6 October 2026, not recovered packet or scoop measurements. The adaptations have not been kitchen-tested.

For example, army stew uses **400 g tofu**, adjustable from **300 to 600 g**. Choose the lower end when serving other dishes, or the upper end when tofu is a bigger part of the meal. Use the recipe's notes to adjust other ingredients.

- Choose one amount before making the shopping list. Use the default unless the cook's preferences suggest otherwise; do not ask a separate question for every range.
- Scale the chosen amount and both range limits by portions / 5. For 3 portions, the army-stew tofu default is **240 g**, with a **180 to 360 g** range. The shopping list should say **240 g tofu**, unless a different amount was chosen.
- Keep dry, fresh, cooked, drained and shell-on weights distinct. For cooked amounts, use the product's labelled yield to calculate a dry purchase amount and show the conversion, or list ready-cooked food explicitly. For drained amounts, use the packet's drained weight. Never buy the same weight of dry rice or noodles as a stated cooked amount, or treat an unknown packet or scoop as a fixed weight.
- Choose one of the alternatives, such as ramen or rice. Count reserved oil, stock and cooking liquid only once. Combine the selected amounts when an ingredient appears in several meals.
- Keep stated custard and slurry ratios intact. Start with the lower suggested seasoning or thickener amount when the method says to, then taste or check the texture before adding more. Do not scale cooking times or temperatures.

## Cooking checks

This edition uses **°C for oven temperatures** and **cloves for bare garlic counts**; explicitly stated heads of garlic remain heads. Added cooking times are estimates. Follow the doneness check in the method, and measure internal temperatures in the thickest part, away from bone.

| Food | Minimum internal temperature |
| --- | --- |
| Chicken, including mince | 74°C |
| Egg dishes; minced beef or pork | 71°C |
| Fish | 63°C |
| Whole-cut beef or pork | 63°C, followed by a 3-minute rest |
| Reheated leftovers | 74°C |

These endpoints follow [FoodSafety.gov](https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures). For mixed dishes, meet the highest applicable temperature. Seafood methods also follow the [FDA's shellfish checks](https://www.fda.gov/food/buy-store-serve-safe-food/selecting-and-serving-fresh-and-frozen-seafood-safely): discard damaged clams or live clams that do not close when tapped, and discard any that stay closed after cooking.

Rinse dried mushrooms and fungus before soaking. Use the times in each recipe and cook them promptly after soaking. Refrigerate any soak that needs more than 2 hours, following the [Hong Kong Centre for Food Safety guidance](https://www.cfs.gov.hk/english/multimedia/multimedia_pub/multimedia_pub_fsf_200_04.html). Soaking time counts toward total elapsed time even when it overlaps with other preparation.

## Recipe index

### Drinks and desserts (5)

- [Chrysanthemum herbal drink](#chrysanthemum-herbal-drink)
- [Luo han guo herbal drink](#luo-han-guo-herbal-drink)
- [Apple and pear soup without meat](#apple-and-pear-soup-without-meat)
- [Papaya and white fungus dessert](#papaya-and-white-fungus-dessert)
- [Cheng tng](#cheng-tng)

### Soups (18)

- [ABC soup](#abc-soup)
- [Apple and pear pork rib soup](#apple-and-pear-pork-rib-soup)
- [Apple and fig soup with lily bulbs](#apple-and-fig-soup-with-lily-bulbs)
- [Chicken and fish maw soup](#chicken-and-fish-maw-soup)
- [Pumpkin and tomato chicken soup](#pumpkin-and-tomato-chicken-soup)
- [Lotus root pork rib soup](#lotus-root-pork-rib-soup)
- [Cordyceps chicken soup](#cordyceps-chicken-soup)
- [White fungus and pear chicken soup](#white-fungus-and-pear-chicken-soup)
- [Winter melon soup with chicken or pork](#winter-melon-soup-with-chicken-or-pork)
- [Old cucumber soup with chicken or pork](#old-cucumber-soup-with-chicken-or-pork)
- [Chayote and sweet corn soup with chicken or pork](#chayote-and-sweet-corn-soup-with-chicken-or-pork)
- [Herbal chicken soup](#herbal-chicken-soup)
- [Liu wei pork soup](#liu-wei-pork-soup)
- [Fish soup](#fish-soup)
- [Pumpkin and chestnut soup](#pumpkin-and-chestnut-soup)
- [Watercress pork rib soup](#watercress-pork-rib-soup)
- [Daikon and carrot pork rib soup](#daikon-and-carrot-pork-rib-soup)
- [Army stew](#army-stew)

### Vegetable dishes (15)

- [Eggplant and broccoli](#eggplant-and-broccoli)
- [Eggplant with minced meat](#eggplant-with-minced-meat)
- [Broccoli with egg slurry](#broccoli-with-egg-slurry)
- [Mixed vegetables](#mixed-vegetables)
- [Chinese yam or lotus root with mixed vegetables](#chinese-yam-or-lotus-root-with-mixed-vegetables)
- [Nonya cabbage](#nonya-cabbage)
- [Stir-fried cabbage](#stir-fried-cabbage)
- [Roasted cabbage](#roasted-cabbage)
- [Stir-fried bok choy with eggs](#stir-fried-bok-choy-with-eggs)
- [Leafy vegetables with garlic - version 1](#leafy-vegetables-with-garlic-version-1)
- [Leafy vegetables with garlic - version 2](#leafy-vegetables-with-garlic-version-2)
- [Bitter gourd with tofu and eggs](#bitter-gourd-with-tofu-and-eggs)
- [Steamed okra](#steamed-okra)
- [Steamed spinach with broth](#steamed-spinach-with-broth)
- [Japanese stir-fried lotus root and tau kwa](#japanese-stir-fried-lotus-root-and-tau-kwa)

### Fish and eggs (18)

- [Japanese steamed egg](#japanese-steamed-egg)
- [Steamed egg with minced chicken or pork](#steamed-egg-minced-meat)
- [Minced pork omelette](#minced-pork-omelette)
- [Red onion omelette](#red-onion-omelette)
- [Otah egg](#otah-egg)
- [Taiwanese dan bing](#taiwanese-dan-bing)
- [Miso mushroom fish](#miso-mushroom-fish)
- [Steamed pomfret](#steamed-pomfret)
- [Steamed dory fillet](#steamed-dory-fillet)
- [Maple-baked miso halibut](#honey-baked-miso-halibut)
- [Steamed halibut with garlic and ginger sauce](#steamed-halibut-garlic-ginger)
- [Tomato egg](#tomato-egg)
- [Fried egg with shallots and spring onion](#fried-egg-shallots-spring-onion)
- [Baked tomato fish in foil](#baked-tomato-fish-foil)
- [Baked salmon with teriyaki sauce](#baked-salmon-teriyaki)
- [Ginger soy fish with baked salmon](#ginger-soy-baked-salmon)
- [Japanese creamy fish stew](#japanese-creamy-fish-stew)
- [Sweet and sour fried tofu](#sweet-sour-fried-tofu-fish)

### Chicken, pork and beef (12)

- [Steamed tofu and egg with pork](#steamed-tofu-egg-pork)
- [Miso mapo tofu](#miso-mapo-tofu)
- [Steamed chicken with mushrooms and black fungus](#steamed-chicken-mushrooms-black-fungus)
- [Braised chicken with mushrooms and tau kwa](#braised-chicken-mushrooms-tau-kwa)
- [Soya chicken and potato stew](#soya-chicken-potato-stew)
- [Baked honey soy chicken](#baked-honey-soy-chicken)
- [Potatoes and carrots with minced meat](#potatoes-carrots-minced-meat)
- [Beef or pork tomato stew](#beef-pork-tomato-stew)
- [Minced beef for tacos](#minced-beef-tacos)
- [Japanese pork stew](#japanese-pork-stew)
- [Garlicky stir-fried beef](#garlicky-stir-fried-beef)
- [Sweet and sour pork ribs](#sweet-sour-pork-ribs)

### Mains (rice and noodles) (23)

- [Fried brown rice with chicken](#fried-brown-rice-chicken)
- [Fried basmati rice with chicken and seafood](#fried-basmati-rice-chicken-seafood)
- [Fried brown rice, reduced seasoning](#fried-brown-rice-reduced-seasoning)
- [Miso butter corn fried rice with chicken](#miso-butter-corn-fried-rice-chicken)
- [Soya mee soup](#soya-mee-soup)
- [Vietnamese beef noodle soup](#vietnamese-beef-noodle-soup)
- [Coconut chicken noodle soup](#coconut-chicken-noodle-soup)
- [Oyakodon](#oyakodon)
- [Ginger scallion chicken rice noodles](#ginger-scallion-chicken-rice-noodles)
- [Soy milk ramen](#soy-milk-ramen)
- [Stir-fried beehoon with fish or chicken](#stir-fried-beehoon-fish-chicken)
- [Tomato curry udon](#tomato-curry-udon)
- [Seafood white beehoon](#seafood-white-beehoon)
- [White braised Hokkien mee](#white-braised-hokkien-mee)
- [Dashi garlic butter fried rice](#dashi-garlic-butter-fried-rice)
- [Pumpkin rice](#pumpkin-rice)
- [Tomato pasta sauce using bottled sauce](#tomato-pasta-sauce-bottled)
- [Homemade tomato pasta sauce](#tomato-pasta-sauce-homemade)
- [Bolognese pasta](#bolognese-pasta)
- [Creamy chicken macaroni soup](#creamy-chicken-macaroni-soup)
- [Japanese sushi and onigiri](#japanese-sushi-onigiri)
- [Korean kimbap](#korean-kimbap)
- [Mexican wraps](#mexican-wraps)

### For kids (12)

- [Yoghurt pancakes](#yoghurt-pancakes)
- [Baked salmon and sweet potato nuggets](#baked-salmon-sweet-potato-nuggets)
- [Tofu meatballs](#tofu-meatballs)
- [Fish, pumpkin, and scallop porridge](#fish-pumpkin-scallop-porridge)
- [Fish, wolfberry, and carrot porridge](#fish-wolfberry-carrot-porridge)
- [Minced pork and carrot porridge](#minced-pork-carrot-porridge)
- [Minced chicken and vegetable porridge](#minced-chicken-vegetable-porridge)
- [Beef and sweet potato porridge](#beef-sweet-potato-porridge)
- [Chicken drumstick soup with carrot, leek, and potato](#chicken-drumstick-soup-carrot-leek-potato)
- [Chicken drumstick soup with carrot, potato, and tomato](#chicken-drumstick-soup-carrot-potato-tomato)
- [Chicken rice with cauliflower](#chicken-rice-cauliflower)
- [Fried rice for kids](#fried-rice-kids)

### Archive (1)

- [Tomato egg soup with mee sua](#tomato-egg-soup-mee-sua)

## Source preparation notes for review

These preparation notes come from the supplied document and await review.

- Soak vegetables in salt and baking soda for 15 minutes, then rinse before cooking. The source gives no salt or baking-soda amount.
- Soak herbs such as red dates and wolfberries with cornflour for 5 minutes, then rinse before cooking. The source gives no cornflour amount.
- Soak dried shrimp, scallops and anchovies with cornflour for 5 minutes, then rinse before cooking. The source describes this as removing dirt. Some individual recipes specify different soaking times.
- Simmer soup bones in boiling water with 2 slices of ginger for 5 minutes, then rinse before adding them to soup.
- The source says minced meat must not be washed.
- The source says to check when unsure.

## Drinks and desserts

<a id="chrysanthemum-herbal-drink"></a>

### Chrysanthemum herbal drink

**ID:** `chrysanthemum-herbal-drink`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Chrysanthemum, quantity not specified
- 4 dates
- 1 honey date
- 1/2 bowl jinyinhua
- 2 sticks liquorice root (gancao)

#### Method

Not specified in source.

#### Notes

The type of dates, bowl size, water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="luo-han-guo-herbal-drink"></a>

### Luo han guo herbal drink

**ID:** `luo-han-guo-herbal-drink`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 2 large luo han guo or 3 small
- 2 sticks liquorice root (gancao)
- 1/2 bowl jinyinhua
- 1 bowl Spica prunellae (xia gu cao)
- 1/2 bowl chrysanthemum (optional)

#### Method

Not specified in source.

#### Notes

Bowl sizes, water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="apple-and-pear-soup-without-meat"></a>

### Apple and pear soup without meat

**ID:** `apple-and-pear-soup-without-meat`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Barley, quantity not specified
- 1 apple
- 1 pear
- 1 honey date
- 1/2 large onion
- 2 cloves garlic

#### Method

Not specified in source.

#### Notes

Water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="papaya-and-white-fungus-dessert"></a>

### Papaya and white fungus dessert

**ID:** `papaya-and-white-fungus-dessert`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Papaya, quantity not specified
- White fungus, quantity not specified
- Red dates, quantity not specified
- Wolfberries, quantity not specified
- Small piece of ginger, size not specified
- Barley, quantity not specified
- Pandan leaves, quantity not specified
- Peach gum, quantity not specified

#### Method

Not specified in source.

#### Notes

The source does not give measured quantities, water quantity or a method.

#### Source

Supplied recipe document.

<a id="cheng-tng"></a>

### Cheng tng

**ID:** `cheng-tng`

**Servings:** 5 portions.

**Time:** Peach resin soaking: at least 8 hours. Pang dahai soaking: 30 minutes. Simmering stages: 30, 30 and 10 minutes.

**Review:** Imported draft.

#### Ingredients

- 1/4 cup peach resin (tao jiao)
- 12 pang dahai
- 8 red dates
- 2 pandan leaves, tied in a knot
- 3 tbsp lotus, form not specified
- 4 melon sticks
- 3 tbsp longan
- 1/2 cup barley

#### Method

1. Soak the peach resin in hot water for at least 8 hours and remove dirt.
2. Soak the pang dahai in hot water for 30 minutes and remove the seeds.
3. Bring the red dates, pandan leaves, lotus and melon sticks to a boil, then simmer for 30 minutes.
4. Add the longan, barley and peach resin. Simmer for 30 minutes.
5. Add the pang dahai jelly and simmer for 10 minutes.

#### Notes

The water quantity, cup size, form of lotus and whether the longan is fresh or dried are not specified. Soaking instructions are retained from the source for review.

#### Source

- [Original source](https://www.recipesaresimple.com/recipe/cheng-tng-healthy-singapore-dessert/)

## Soups

<a id="abc-soup"></a>

### ABC soup

**ID:** `abc-soup`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients


**Potato variant**

- 2 potatoes
- 1 yellow onion
- 1 carrot
- 1 corn
- 1 large tomato
- Pork ribs or chicken bones, quantity not specified

**Chinese yam variant**

- 1 Chinese yam
- 1 carrot
- 1 corn
- 1 onion
- Pork ribs or chicken bones, quantity not specified
- 5 red dates

#### Method

Not specified in source.

#### Notes

The source gives two separate ingredient lists. Choose one variant rather than combining them. Water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="apple-and-pear-pork-rib-soup"></a>

### Apple and pear pork rib soup

**ID:** `apple-and-pear-pork-rib-soup`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 300 g pork ribs
- 2 apples
- 1 pear
- 5 red dates
- 2 dried figs
- 2 tbsp sweet apricot kernels
- 1 tbsp bitter kernels, type unclear in the source
- 1/2 white fungus, unit not specified
- 1 tbsp goji berries

#### Method

Not specified in source.

#### Notes

The source says only "1 tbsp bitter". Confirm the kernel type and preparation. Water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="apple-and-fig-soup-with-lily-bulbs"></a>

### Apple and fig soup with lily bulbs

**ID:** `apple-and-fig-soup-with-lily-bulbs`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 2 apples or pears
- 8 figs
- 1 tbsp bitter almond kernels, as named in the source
- 2 tbsp sweet almond kernels, as named in the source
- 1/2 small bowl lily bulbs
- 1/3 white fungus, unit not specified
- Pork ribs (optional), quantity not specified

#### Method

Not specified in source.

#### Notes

Confirm the kernel identities and preparation before use. The form of figs, bowl size, water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="chicken-and-fish-maw-soup"></a>

### Chicken and fish maw soup

**ID:** `chicken-and-fish-maw-soup`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 1/2 stick fish maw
- Chicken bones, quantity not specified
- 250 g fresh Chinese yam (huai shan)
- About 8-10 medium pieces yu zhu
- 1 corn
- 1 carrot
- 6 red dates
- 1 tbsp wolfberries

#### Method

Not specified in source.

#### Notes

Water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="pumpkin-and-tomato-chicken-soup"></a>

### Pumpkin and tomato chicken soup

**ID:** `pumpkin-and-tomato-chicken-soup`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 500 g chicken bones or thighs
- 2 tomatoes
- 1 carrot
- 1 corn
- 2 scallops (optional)

#### Method

Not specified in source.

#### Notes

The title names pumpkin, but pumpkin is absent from the ingredient list. Confirm whether to include it and in what quantity. The form of scallops, water quantity and method are not specified.

#### Source

- [Original source](https://www.instagram.com/reel/C4PC-aAS6hc/)

<a id="lotus-root-pork-rib-soup"></a>

### Lotus root pork rib soup

**ID:** `lotus-root-pork-rib-soup`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Pork rib bones, quantity not specified
- 1 tbsp lotus, form not specified
- 1/2 cup black beans, or 1 corn if black beans are unavailable
- 1/2 cup walnuts
- 6 red dates
- 2 carrots
- 3 scallops

#### Method

Not specified in source.

#### Notes

The title names lotus root, while the ingredient list says "1 tbsp lotus". Confirm the ingredient and amount. The form of scallops, water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="cordyceps-chicken-soup"></a>

### Cordyceps chicken soup

**ID:** `cordyceps-chicken-soup`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 1 sweet corn
- 6 red dates
- 1 carrot
- 6 dried shiitake mushrooms
- 1 sweet date
- 800 g chicken (drumsticks and bones)
- Fresh cordyceps, quantity not specified
- 4-5 dried Chinese yam, unit not specified

#### Method

Not specified in source.

#### Notes

Water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="white-fungus-and-pear-chicken-soup"></a>

### White fungus and pear chicken soup

**ID:** `white-fungus-and-pear-chicken-soup`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 1 whole chicken bone, as written in the source
- 2 scallops
- 1 snow pear
- 1/2 snow fungus, unit not specified
- 1 brown snow pear
- 1 carrot
- 3 dried figs
- 4 red dates
- 1 tsp wolfberries
- Lotus seeds, quantity not specified
- 1/2 bowl small barley

#### Method

Not specified in source.

#### Notes

Confirm what "1 whole chicken bone" means. The source lists both a snow pear and a brown snow pear. The form of scallops, bowl size, water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="winter-melon-soup-with-chicken-or-pork"></a>

### Winter melon soup with chicken or pork

**ID:** `winter-melon-soup-with-chicken-or-pork`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Pork or chicken bones, quantity not specified
- Winter melon, quantity not specified
- 1 sweet corn
- 1 carrot
- 4 dried scallops
- 6 red dates
- 1 tbsp wolfberries
- 5 dried Chinese yam, unit not specified

#### Method

Not specified in source.

#### Notes

Water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="old-cucumber-soup-with-chicken-or-pork"></a>

### Old cucumber soup with chicken or pork

**ID:** `old-cucumber-soup-with-chicken-or-pork`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 350 g meat, source allows any meat
- 1 old cucumber
- 1 tbsp Chinese pearl barley
- 1 tbsp green mung beans
- 2 honey dates
- 2000 ml water

#### Method

Not specified in source.

#### Notes

The source suggests choosing a heavy, wrinkled old cucumber and claims higher nutritional value. That nutritional claim needs review. A cooking method is not specified.

#### Source

- [Original source](https://www.instagram.com/p/C38_Qt0yyu7/)

<a id="chayote-and-sweet-corn-soup-with-chicken-or-pork"></a>

### Chayote and sweet corn soup with chicken or pork

**ID:** `chayote-and-sweet-corn-soup-with-chicken-or-pork`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 1-2 chayotes
- 1 sweet corn
- 2 tbsp (20 g) dried lily bulbs
- 5 pieces dried Chinese yam
- 2 tbsp (20 g) qian shi
- 1 small dried tangerine peel
- 2 candied dates
- 350 g soup meat
- 2500 ml water

#### Method

Not specified in source.

#### Notes

A cooking method is not specified.

#### Source

- [Original source](https://www.instagram.com/reel/C4g7Tq1y9iQ/)

<a id="herbal-chicken-soup"></a>

### Herbal chicken soup

**ID:** `herbal-chicken-soup`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Chicken bones, quantity not specified
- 5 dried Chinese yam, unit not specified
- 4 red dates
- 1 tbsp wolfberries
- 4 pieces astragalus root (huang qi)
- About 10 pieces yu zhu
- 4-5 dang shen, unit not specified
- 1 tbsp lotus seeds (optional)
- 1 tbsp lily bulbs (optional)

#### Method

Not specified in source.

#### Notes

The source labels this recipe "Not suitable for kids". Retain that restriction pending ingredient and suitability review. Water quantity and method are not specified.

#### Source

Supplied recipe document.

<a id="liu-wei-pork-soup"></a>

### Liu wei pork soup

**ID:** `liu-wei-pork-soup`

**Servings:** 5 portions.

**Time:** Low-heat cooking: 2 hours. Add longan after 1 hour and qi zi in the final 5 minutes.

**Review:** Imported draft.

#### Ingredients


**Group A**

- 20 g 玉竹 (yu zhu)
- 20 g 干百合 (dried lily bulbs)
- 20 g 芡实 (fox nuts)
- 20 g 淮山 (huai shan)
- 20 g 湘莲 (lotus seeds)
- 6 红枣 (red dates), seeds removed
- 250 g lean pork
- 1000 ml water

**Group B**

- 2 tbsp (20 g) 圆肉 (dried longan)
- 2 tbsp 杞子 (qi zi)

**To finish**

- Salt, to taste

#### Method

1. Rinse the lean pork, cut it into large pieces and scald it.
2. Rinse the remaining ingredients and bring the water to a boil.
3. Add Group A and return to a boil over high heat.
4. Reduce to low heat and cook for 2 hours.
5. Add the dried longan after 1 hour. Add the qi zi 5 minutes before the end of the 2 hours.
6. Add salt to taste and serve.

#### Notes

The source says longan and qi zi can make the soup sour if cooked too long. The scalding time is not specified.

#### Source

Supplied recipe document.

<a id="fish-soup"></a>

### Fish soup

**ID:** `fish-soup`

**Servings:** 5 portions.

**Time:** Baking: 25 minutes. Simmering: 4 hours.

**Review:** Imported draft.

#### Ingredients

- 500 g fish bones (white fish or grouper)
- 200 g sliced fish
- 200 g chicken bones
- 5 large slices ginger in the ingredient list; the method calls for 10 slices
- 1 onion
- 1 sprig spring onion
- 50 g pumpkin (optional)
- 1/2 cup yellow soybeans (optional)
- 1/2 cup anchovies (optional)
- 1 tbsp cornstarch, from the method
- Olive oil, quantity not specified, from the method
- Carrots, quantity not specified, from the method
- Coriander root, quantity not specified, from the method
- Spinach/cabbage noodles, as written in the serving note; quantity not specified
- Eggs, quantity not specified, for serving
- 1 tsp fish seasoning, for the sliced fish
- 1/2 tsp sesame oil, for the sliced fish
- Ginger juice, quantity not specified, for the sliced fish

#### Method

1. The source instructs mixing the fish bones with 10 slices ginger, spring onions and 1 tbsp cornstarch, then washing the mixture off.
2. Coat the fish bones with olive oil and bake for 25 minutes at 225°C.
3. Simmer the fish bones with the chicken bones, yellow soybeans, carrots, onion, coriander root and anchovies for 4 hours.
4. Marinate the sliced fish with the fish seasoning, sesame oil and ginger juice.
5. The source says to serve with spinach/cabbage noodles, eggs and the marinated sliced fish. It does not provide the final cooking steps for these ingredients.

#### Notes

Confirm the ginger amount and water quantity before cooking. Pumpkin appears in the ingredient list but has no method step. "Spinach/cabbage noodles" is ambiguous. The final cooking method for the sliced fish and eggs is missing; this is an incomplete method.

#### Source

- [Original source 1](https://www.saveur.com/article/Recipes/Double-Rich-Fish-Stock/)
- [Original source 2](https://eatwhattonight.com/2019/12/pumpkin-and-grouper-fish-soup/)

<a id="pumpkin-and-chestnut-soup"></a>

### Pumpkin and chestnut soup

**ID:** `pumpkin-and-chestnut-soup`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Chicken or pork bones, quantity not specified
- 300 g pumpkin
- 10 dried chestnuts
- 1 carrot
- 1 corn
- 2 honey dates
- 6 dried Chinese yam, unit not specified
- 2 tbsp Euryale seeds

#### Method

Not specified in source.

#### Notes

Water quantity and method are not specified.

#### Source

- [Original source](https://www.instagram.com/p/DAi2H2TS7zH/)

<a id="watercress-pork-rib-soup"></a>

### Watercress pork rib soup

**ID:** `watercress-pork-rib-soup`

**Servings:** 5 portions.

**Time:** Anchovy soaking: 15 minutes. Add watercress in the final 15 minutes. Total cooking time not specified.

**Review:** Imported draft.

#### Ingredients

- 300 g pork ribs
- 1 carrot
- 6 medium dried scallops
- 3 tbsp wolfberries
- 1/2 bowl anchovies
- Cornflour, quantity not specified, for the source soaking instruction
- 1 honey date (optional)
- 6 medium red dates, seeds removed
- 2500 ml water
- 1 bunch watercress

#### Method

1. The source instructs soaking the anchovies with cornflour for 15 minutes, then rinsing them with water.
2. Add the watercress in the final 15 minutes of cooking.

#### Notes

The source provides only preparation and finishing instructions. It does not specify how or how long to cook the soup base. The anchovy soaking instruction and bowl size need review.

#### Source

Supplied recipe document.

<a id="daikon-and-carrot-pork-rib-soup"></a>

### Daikon and carrot pork rib soup

**ID:** `daikon-and-carrot-pork-rib-soup`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 300 g pork ribs
- 1 radish (daikon)
- 1 carrot
- 1/2 Japanese leek (optional)
- 1 yellow onion
- 3 slices ginger
- 2 garlic cloves, smashed
- 6 medium dried mushrooms, rehydrated and sliced; retain the soaking liquid
- 3000-4000 ml water

#### Method

1. Fry the ginger, garlic and optional leek, then brown the pork ribs.
2. Add the water, onion, mushrooms and mushroom soaking liquid, then simmer.

#### Notes

The method omits when to add the daikon and carrot and gives no simmering duration.

#### Source

Supplied recipe document.

<a id="army-stew"></a>

### Army stew

**ID:** `army-stew`

**Servings:** 5 portions.

**Time:** Suggested estimate: 15 minutes preparation and 20 minutes cooking, plus rice cooking if using rice.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 400 g silken tofu, drained and cubed; adjust from 300 to 600 g
- 150 g enoki mushrooms, roots trimmed; adjust from 100 to 200 g
- 1 cup kimchi, roughly chopped
- 20 g sliced cheese, optional; omit or use up to 40 g
- 1 litre low-sodium broth
- 150 g peeled onion, sliced; adjust from 100 to 200 g
- 5 g dried kombu and 5 g bonito flakes, or a dashi sachet labelled for 1 litre; choose one stock-flavouring option
- 75 g trimmed leek, sliced and rinsed; adjust from 50 to 100 g
- 3 garlic cloves, minced
- 1 tbsp mirin
- 2 tbsp gochujang
- 1/2 tbsp oyster sauce
- 1 tbsp sesame oil
- 1 tbsp gochugaru, optional for more spice
- 2 tbsp ketchup; use up to 3 tbsp, or replace with 250 g canned baked beans in their sauce; use 200 to 400 g
- 300 g dry ramen, cooked separately; adjust from 250 to 350 g
- Alternatively, 750 g cooked rice; adjust from 650 to 1,000 g
- Hot water, in 100 ml additions if more broth is needed

#### Method

1. Put the broth, onion, leek and kombu in a pot. Heat gently and remove the kombu just before the broth boils. If using a dashi sachet, follow its steeping instructions and remove it. Simmer the onion and leek for about 8 minutes, until softened.
2. If using kombu, add the bonito flakes in a stock bag or fine-mesh infuser. Steep for 3 minutes, then remove them. Skip the bonito when using a dashi sachet. Stir in the garlic, mirin, gochujang, oyster sauce, sesame oil, optional gochugaru and ketchup or baked beans.
3. Add the kimchi, tofu and enoki. Bring back to a simmer and cook for 5 to 8 minutes, until the mushrooms are cooked and the tofu is hot throughout.
4. Meanwhile, cook the ramen in a separate pot according to its packet, then drain. If using rice, have it cooked and hot before serving.
5. Taste the stew. Add hot water in 100 ml amounts if needed, then taste again before adding seasoning. Add the optional cheese and let it melt. Divide the stew and noodles or rice among five portions.

#### Notes

- Suggested amounts replace the undefined packets and ingredient quantities. These are practical defaults, not recovered measurements from the original notes.
- Use 300 g tofu when this stew accompanies other dishes, or 600 g for a tofu-heavy meal. More enoki adds texture; more cheese makes the broth richer.
- Choose noodles or rice, not both by default. Keep noodles separate until serving so they do not absorb the stew's 1 litre of broth.
- Kombu and dashi sachets vary in strength. The dashi alternative must be labelled for 1 litre; do not assume every sachet has the same strength.
- Use kombu with bonito or a dashi sachet. Do not add both options to the broth.

#### Source

Supplied recipe document.

## Vegetable dishes

<a id="eggplant-and-broccoli"></a>

### Eggplant and broccoli

**ID:** `eggplant-and-broccoli`

**Servings:** 5 portions.

**Time:** Steaming: 5 minutes.

**Review:** Imported draft.

#### Ingredients

- 4 garlic cloves, minced
- 3 sprigs basil
- 3 medium tomatoes
- 1 shallot, sliced
- 2 spring onions, white parts
- 1 large eggplant
- 1/2 head broccoli, optional status unclear in the source

**Stir-fry seasoning**

- 1 tbsp hoisin sauce
- 1 tbsp soy sauce
- 1/2 tsp brown sugar or 1 tsp wolfberries

#### Method

1. Steam the eggplant for 5 minutes.
2. Stir-fry with the other ingredients and stir-fry seasoning.

#### Notes

The source places "optional" after the eggplant and broccoli line without identifying which ingredient it applies to. The stir-frying duration is not specified.

#### Source

Supplied recipe document.

<a id="eggplant-with-minced-meat"></a>

### Eggplant with minced meat

**ID:** `eggplant-with-minced-meat`

**Servings:** 5 portions.

**Time:** Eggplant cooking: 15 minutes. Simmering: 3 minutes.

**Review:** Imported draft.

#### Ingredients

- 2 medium eggplants, cut into fries
- 1/2 leek, sliced
- 2 garlic cloves, minced
- 3 slices ginger, cut into strips
- 200 g minced chicken or pork
- Salt, quantity not specified, from the method

**Stir-fry seasoning**

- Dark soy sauce, to taste
- 1/2 tsp fish sauce
- 1 tbsp hoisin sauce
- 30 g water, as measured in the source
- 1 tbsp cornstarch slurry, from the method; mixture ratio not specified

#### Method

1. Salt the eggplant, then "air fry" it in the oven for 15 minutes until soft, as described in the source.
2. Fry the garlic, ginger and leek. Add the minced meat and cook until brown.
3. Add the eggplant and seasoning. Simmer for 3 minutes.
4. Thicken with 1 tbsp cornstarch slurry.

#### Notes

The oven/air-fryer setting and temperature are not specified. Confirm the intended appliance setting. The source measures water in grams; that amount is retained. Slurry proportions are missing.

#### Source

- [Original source](https://www.instagram.com/reel/DKfJf-KSkfl/)

<a id="broccoli-with-egg-slurry"></a>

### Broccoli with egg slurry

**ID:** `broccoli-with-egg-slurry`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 1 head broccoli
- 3 garlic cloves, sliced
- 2 eggs
- 1 tbsp wolfberries
- Black fungus (optional), quantity not specified

**Seasoning**

- 1 tsp soy sauce
- 1 tsp fish sauce
- 2 tsp Chinese wine
- 125 ml water
- 1/2 tsp cornflour

#### Method

1. Pan-fry the broccoli with the garlic and set aside.
2. Add the seasoning and wolfberries, then simmer.
3. Thicken with the 1/2 tsp cornflour.
4. When the sauce is ready, drizzle in the eggs.

#### Notes

The source does not say when to return the broccoli, how to add the optional black fungus, or how long to cook the eggs. The final cooking duration is missing.

#### Source

Supplied recipe document.

<a id="mixed-vegetables"></a>

### Mixed vegetables

**ID:** `mixed-vegetables`

**Servings:** 5 portions.

**Time:** Suggested: 10 minutes preparation and 10 minutes cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

**Default four main ingredients**

- 1/2 head broccoli, cut into small florets
- 1/2 head cauliflower, cut into small florets
- 100 g fresh baby corn, halved lengthways; use 75 to 150 g
- 75 g fresh shimeji mushrooms, weighed after trimming the roots, clusters separated; use 50 to 150 g

**Optional swaps**

- Replace one of the four ingredients above with 1/2 carrot, thinly sliced, or 200 g tau kwa, cubed; use 150 to 250 g tau kwa

**Aromatics and seasoning**

- 1 tbsp cooking oil
- 4 slices ginger
- 2 garlic cloves, minced
- 100 ml water, plus 1 tbsp at a time if the pan dries before the vegetables soften
- 1 tsp oyster sauce
- 1 tbsp wolfberries, rinsed
- 1 tsp light soy sauce

**Slurry**

- 3/4 tsp cornstarch
- 1 tbsp cold water

#### Method

1. Choose the four main ingredients, using the default selection or one of the swaps. Cut broccoli and cauliflower into small florets so they cook evenly.
2. Heat the oil over medium heat. Saute the ginger and garlic for about 30 seconds until fragrant.
3. Add the baby corn and any carrot or thick vegetable stems first. Toss for 1 minute, then add the florets, mushrooms and any tau kwa.
4. Add the 100 ml water, oyster sauce, wolfberries and soy sauce. Cover and simmer for 3 to 5 minutes, until the vegetables are tender enough for your preference and the mushrooms are cooked. Add water 1 tbsp at a time if needed.
5. Mix the cornstarch with its cold water. Stir again, add half to the simmering vegetables, and stir until the sauce thickens. Add the rest only if needed to coat the vegetables, then simmer for about 1 minute and serve.

#### Notes

- Baby-corn, shimeji and tau-kwa weights are suggested amounts, not conversions of the original packets or piece count. More mushrooms or tofu make the shared side dish more substantial.
- The default uses four main ingredients. Optional carrot or tau kwa replaces one of them; do not add every listed option to the shopping list.
- The measured frying oil, ingredient order and tenderness check complete the short source method. The original slurry ratio is retained.

#### Source

- [Original source](https://cookwithmi.wixsite.com/cookwithmi/post/cookwithmi-claypot-egg-tofu-with-assorted-vegetables)

<a id="chinese-yam-or-lotus-root-with-mixed-vegetables"></a>

### Chinese yam or lotus root with mixed vegetables

**ID:** `chinese-yam-or-lotus-root-with-mixed-vegetables`

**Servings:** 5 portions.

**Time:** Suggested: 20 minutes preparation and 12 minutes cooking, plus 20 to 30 minutes black-fungus soaking, which can overlap with preparation.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 1/2 broccoli, cut into small florets
- 1/2 carrot, thinly sliced
- 100 g snow peas, trimmed; use 75 to 150 g
- 200 g peeled Chinese yam or lotus root, thinly sliced; use 150 to 250 g
- 2 celery sticks, peeled and thinly sliced diagonally
- 5 g dried black fungus; use 3 to 8 g, weighed before soaking
- 60 g toasted cashew nuts, as a working amount for the original 1/2 cup
- 4 slices ginger
- 1 tsp minced garlic
- 2 tsp neutral cooking oil
- 1 tbsp sesame oil
- Water to cover the fungus generously for soaking, and separate water to cover the sliced root for boiling

**Sauce**

- 1 1/2 tbsp oyster sauce or abalone sauce
- 120 ml water, as a working amount for the original 1/2 cup
- 1 tbsp wolfberries or 1/2 tsp sugar

#### Method

1. Rinse the black fungus and soak in enough clean water to cover generously for about 20 to 30 minutes, until expanded and flexible; follow its label if it needs longer. Follow the collection's soaking guidance. Drain, rinse, trim off hard bases and tear into bite-sized pieces. Do not use the soaking water.
2. Mix the sauce ingredients. The sliced celery can go straight into the pan; the original unspecified celery-soaking step is omitted.
3. Boil the Chinese yam slices for about 3 minutes, or lotus-root slices for about 5 minutes, until almost tender. Drain.
4. Heat the neutral oil in a large wok. Fry the ginger and garlic for about 30 seconds. Add the broccoli, carrot and celery; stir-fry for 2 to 3 minutes. Add the drained yam or lotus root, snow peas and fungus; stir-fry for another 2 minutes.
5. Add the sauce, cover and simmer for about 3 minutes, until the vegetables are cooked but retain some bite. Uncover and reduce excess sauce briefly if needed.
6. Toss through the sesame oil and cashews, then serve.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- The snow-pea, dried-fungus and peeled-root weights replace undefined packets and variable root sizes. More snow peas or root makes a larger vegetable dish; use less fungus for a lighter texture.
- Both cup measures use a suggested 240 ml household cup. The cashew weight is a working amount rather than an exact conversion from the original notes.

#### Source

Supplied recipe document.

<a id="nonya-cabbage"></a>

### Nonya cabbage

**ID:** `nonya-cabbage`

**Servings:** 5 portions.

**Time:** Ingredient soaking: 15 minutes. Simmering: 15 minutes.

**Review:** Imported draft.

#### Ingredients

- 1/3 Wongbok cabbage, cut into large pieces
- 4 dried black fungus, soaked for 15 minutes
- 1 long stick dried beancurd, soaked for 15 minutes (optional)
- 4 dried mushrooms, soaked for 15 minutes
- 1 tbsp dried shrimp, soaked for 15 minutes
- 50 g pork collar, cut into strips (optional)
- 1 handful glass noodles
- 1 tbsp oyster sauce
- 150 ml mushroom soaking liquid
- Garlic, quantity not specified, from the method

#### Method

1. Stir-fry the garlic, dried shrimp and optional pork.
2. Add the remaining ingredients except the glass noodles, then bring to a boil.
3. Simmer for 15 minutes, then add the glass noodles and serve.

#### Notes

The source does not specify glass-noodle preparation or a cooking step after adding them. Review this before using the method.

#### Source

Supplied recipe document.

<a id="stir-fried-cabbage"></a>

### Stir-fried cabbage

**ID:** `stir-fried-cabbage`

**Servings:** 5 portions.

**Time:** Suggested: 30 to 60 minutes mushroom soaking, with 15 minutes shrimp soaking and preparation during that time, then 15 to 20 minutes cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 1/2 large napa cabbage, cut into strips, with stems and leaves separated
- 1/2 carrot, grated or cut into thin strips
- 3 large dried shiitake mushrooms
- 300 ml warm water, for soaking the mushrooms; reserve 100 ml after straining
- 2 garlic cloves, minced
- 1 tsp small dried shrimp
- Warm water to cover the shrimp in a separate small bowl; discard after soaking
- 1 tbsp cooking oil
- 1/2 tsp oyster sauce

#### Method

1. Rinse the dried mushrooms. Soak them in 300 ml warm water for about 30 minutes, or up to 60 minutes if needed, until soft throughout. Remove tough stalks and slice the caps. Strain the soaking liquid through a fine sieve and measure 100 ml for the pan. Top up with plain water if less remains; do not add all the soaking water.
2. Meanwhile, rinse the dried shrimp and soak separately in enough warm water to cover for 15 minutes, until softened. Drain, discard their soaking water, then smash and finely chop the shrimp.
3. Heat the cooking oil over medium heat. Fry the garlic and shrimp for about 1 minute until fragrant.
4. Add the cabbage stems, carrot and sliced mushrooms. Stir-fry for 2 minutes, then add the cabbage leaves, measured 100 ml mushroom liquid and oyster sauce.
5. Cover and simmer gently for 10 to 15 minutes, stirring occasionally, until the carrot and cabbage stems are soft and the mushrooms are cooked. Add plain water 1 tbsp at a time only if the pan dries before the vegetables are tender.

#### Notes

- This adaptation identifies the soaked small shrimp as dried shrimp and supplies soaking times, soaking water and frying oil. The original 100 ml cooking liquid is retained.
- Thick mushrooms may need longer soaking. Follow the product instructions if they differ and refrigerate any soak that needs more than 2 hours. The listed cooking time does not include unattended soaking.

#### Source

Supplied recipe document.

<a id="roasted-cabbage"></a>

### Roasted cabbage

**ID:** `roasted-cabbage`

**Servings:** 5 portions.

**Time:** Suggested: 10 minutes preparation and 25 to 35 minutes cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 1/2 large cabbage, cut into 2 to 3 cm thick wedges with enough core to hold them together
- 75 g fresh oyster mushrooms and 75 g fresh shimeji, weighed after trimming, separated; use 100 to 200 g combined
- 2 tsp olive oil
- 1/8 tsp salt, optional

**Sauce**

- 1 garlic clove, minced
- 1 tsp minced ginger
- 1 tbsp butter
- 1/2 tsp garlic powder
- 1 1/2 tbsp miso
- 60 ml water; add up to 20 ml more if needed
- 30 ml cream or fresh milk

#### Method

1. Heat the oven to 180°C. Toss the cabbage and mushrooms with the olive oil and optional salt. Spread them on a lined roasting tray. Roast for about 20 minutes, turning the cabbage once, until the mushrooms are cooked and the cabbage is tender at its thickest part. Remove the mushrooms first if ready; let thicker cabbage wedges cook longer.
2. While the vegetables roast, melt the butter in a small pan. Fry the garlic and ginger over low heat for about 1 minute, then stir in the garlic powder.
3. Stir the miso into 60 ml water until smooth. Add it to the pan with the cream or milk. Heat gently for 1 to 2 minutes without boiling hard. Add up to 20 ml more water if the sauce is too thick to pour.
4. Transfer all the roasted mushrooms into the sauce and stir to coat. Spoon the mushroom sauce over the roasted cabbage and serve.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- The mushroom weight replaces the unknown half-packet. Use the upper amount for more mushrooms in the sauce.
- All mushrooms roast first, then go into the sauce. This resolves their appearance in both original cooking steps.
- Oil, ginger and the optional small salt amount are suggested additions or clarified quantities. Miso already contributes salt, so taste the sauce before adding any more.

#### Source

Supplied recipe document.

<a id="stir-fried-bok-choy-with-eggs"></a>

### Stir-fried bok choy with eggs

**ID:** `stir-fried-bok-choy-with-eggs`

**Servings:** 5 portions.

**Time:** Suggested: 10 minutes preparation and about 10 minutes cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 350 g bok choy, trimmed, stems and leaves separated; use 250 to 450 g
- 4 eggs
- 1/2 tsp fish sauce
- 1/8 tsp white pepper
- 1 tbsp oyster sauce
- 2 garlic cloves, sliced
- 8 cherry tomatoes, halved
- 100 g fresh baby corn, thinly sliced diagonally; use 75 to 150 g
- 1 tbsp neutral cooking oil, divided
- 2 tbsp water

#### Method

1. Beat the eggs with the fish sauce and white pepper. Cut thicker bok choy stems into bite-sized pieces and keep the leaves separate.
2. Heat half the oil in a large non-stick frying pan over medium heat. Add the eggs and scramble for about 2 minutes, until just set. Transfer to a clean plate; they will finish heating when returned to the pan.
3. Add the remaining oil and garlic. Stir-fry for about 30 seconds, then add the bok choy stems and sliced baby corn. Stir-fry for 2 minutes, add the water, cover and cook for another 2 minutes, until the stems and corn are almost tender.
4. Uncover and add the bok choy leaves, cherry tomatoes and oyster sauce. Stir-fry for about 1 to 2 minutes, until the leaves wilt and the tomatoes soften slightly.
5. Return the eggs, break them into large pieces and toss for about 1 minute, until the vegetables are tender and the egg reaches 71°C throughout. Serve immediately.

#### Notes

- The bok-choy and baby-corn weights, pepper, cooking oil and water are suggested working amounts. They replace an unspecified bunch and missing quantities rather than recover the original measurements. This adaptation has not been kitchen-tested.
- Use more bok choy or baby corn for a larger vegetable side dish. Slice baby corn thinly so it cooks alongside the stems. The original four eggs and sauce amounts are retained.
- Cooking times are estimates. The eggs return at the end so they finish heating without becoming dry.

#### Source

- [Original source](https://www.instagram.com/reel/C3gp0X1SbP7/)

<a id="leafy-vegetables-with-garlic-version-1"></a>

### Leafy vegetables with garlic - version 1

**ID:** `leafy-vegetables-with-garlic-version-1`

**Servings:** 5 portions.

**Time:** Stems: about 3 minutes. Leaves: about 3 minutes.

**Review:** Imported draft.

#### Ingredients

- Kailan, spinach or broccoli, quantity not specified
- 3 garlic cloves, minced or grated
- 1 tsp sesame oil
- 1 tbsp olive oil for stir-frying
- 1 tbsp soy sauce or a pinch of mushroom salt

#### Method

1. Stir-fry the stems separately from the leafy parts until bright green, about 3 minutes.
2. Stir in the garlic, then add the leafy parts.
3. Cook for about 3 minutes until the leaves turn dark green.
4. Toss the stems and garlic over the leaves. Cover with a lid and lower the heat to medium.
5. Season with the soy sauce or mushroom salt and sesame oil before serving.

#### Notes

The source does not specify the amount of vegetables or the duration after covering the pan.

#### Source

Supplied recipe document.

<a id="leafy-vegetables-with-garlic-version-2"></a>

### Leafy vegetables with garlic - version 2

**ID:** `leafy-vegetables-with-garlic-version-2`

**Servings:** 5 portions.

**Time:** Vegetable stir-frying: 1 minute, or until starting to soften.

**Review:** Imported draft.

#### Ingredients

- Kailan, spinach or broccoli, quantity not specified
- 3 garlic cloves, minced or grated
- 1 tsp sesame oil
- 1 tbsp olive oil for stir-frying
- 1 tsp soy sauce
- 1 tbsp oyster sauce
- 1 tbsp Chinese wine
- Cornflour, quantity not specified, from the method
- Water, quantity not specified, for the slurry

#### Method

1. Mix the sauce ingredients in a small bowl. Taste and adjust.
2. In a separate bowl, combine the cornflour and water.
3. Heat a wok over medium heat, then reduce to low heat and add the cooking oil.
4. Stir the garlic continuously until it starts to turn light golden brown. Turn off the heat and remove the garlic with a slotted spoon, leaving its oil in the wok.
5. Reheat the garlic oil over high heat. Add the vegetables and stir-fry vigorously for 1 minute, or until the stems and leaves start to soften.
6. Add the sauce. Stir the slurry again, then add enough to thicken to the desired consistency.
7. Plate, garnish with the fried garlic and serve immediately.

#### Notes

The vegetable amount and slurry proportions are not specified. The source notes that garlic burns quickly after turning golden brown.

#### Source

Supplied recipe document.

<a id="bitter-gourd-with-tofu-and-eggs"></a>

### Bitter gourd with tofu and eggs

**ID:** `bitter-gourd-with-tofu-and-eggs`

**Servings:** 5 portions.

**Time:** Suggested: 15 minutes preparation, 30 minutes soaking and 12 minutes cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 1 bitter gourd, 200 g, seeded and thinly sliced
- 3 eggs, beaten
- 3 garlic cloves, minced
- 1 small onion, thinly sliced
- 200 g tau kwa, drained and cubed; use 150 to 300 g
- 1 tbsp mirin
- 1/4 tsp salt, for seasoning
- 1 tbsp neutral cooking oil, divided
- 3 g bonito flakes, to finish; use 2 to 5 g

**Soaking mixture**

- 500 ml freshly collected rice-rinsing water, or fresh drinking water, enough to cover the bitter gourd
- 1 tsp salt
- 1 tsp sugar

#### Method

1. Stir the soaking salt and sugar into the rice-rinsing water or fresh water. Soak the bitter gourd for 30 minutes, then discard the water, rinse and drain.
2. Heat half the cooking oil in a non-stick frying pan. Fry the tau kwa over medium heat for about 4 to 5 minutes, turning until lightly browned, then set aside.
3. Add the remaining oil, garlic and onion. Fry for about 2 minutes. Add the bitter gourd, mirin and 1/4 tsp seasoning salt. Stir-fry for about 3 minutes, until the bitter gourd is tender with a little bite.
4. Return the tau kwa, pour in the beaten eggs and stir gently for about 2 to 3 minutes, until the eggs are set and reach 71°C throughout.
5. Scatter over the bonito flakes and serve.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- The tau-kwa and bonito weights replace an undefined block and garnish amount. Use more tau kwa for a heartier side dish or less bonito for a milder flavour.
- The soaking-water volume and cooking oil are suggested quantities. Use fresh rice-rinsing water immediately after rinsing rice; fresh drinking water is an alternative.
- The 1/4 tsp salt seasons the stir-fry. The separate soaking salt is discarded with the soaking water.

#### Source

- [Original source](https://www.instagram.com/reel/C36k5hcS6Fu/)

<a id="steamed-okra"></a>

### Steamed okra

**ID:** `steamed-okra`

**Servings:** 5 portions.

**Time:** Suggested: 5 minutes preparation and about 8 minutes steaming.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 250 g okra, washed with only the tough stem tips trimmed; use 200 to 350 g

**Seasoning A**

- 3 g bonito flakes; use 2 to 5 g
- 1 tsp dashi powder
- 1 tsp soy sauce
- 1 tbsp mirin
- 2 tbsp sesame seeds
- 1 tbsp hot water, to dissolve the dashi

**Seasoning B**

- 1 tbsp soy sauce
- 1 tbsp water
- 1/2 tsp sugar
- 2 tsp sesame oil

#### Method

1. Choose seasoning A or B. For A, dissolve the dashi in the hot water and mix in the soy sauce, mirin and sesame seeds. Keep the bonito flakes aside. For B, mix all its ingredients until the sugar dissolves.
2. Place the whole okra in a heatproof dish and steam over simmering water for about 8 minutes, until tender when pierced. Thicker pods may need longer. Drain any water from the dish.
3. Pour over the chosen seasoning. If using A, add the bonito flakes just before serving.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- The okra and bonito weights replace unknown packets. More okra makes a larger side dish; more bonito gives a stronger fish flavour.
- Choose only one seasoning. The hot water in A is a suggested addition to dissolve the powder rather than leave dry granules on the okra.

#### Source

- [Original source](https://www.instagram.com/reel/DMh-AdFxvKb/)

<a id="steamed-spinach-with-broth"></a>

### Steamed spinach with broth

**ID:** `steamed-spinach-with-broth`

**Servings:** 5 portions.

**Time:** Spinach steaming: 5 minutes. Broth simmering: 15 minutes.

**Review:** Imported draft.

#### Ingredients

- 1 bunch Chinese spinach
- 2 tbsp whitebait
- 1 garlic clove, sliced
- 1 tbsp wolfberries
- 1 tbsp dried scallops
- 1 cup water, from the method

#### Method

1. Steam the spinach for 5 minutes.
2. Stir-fry the garlic until fragrant.
3. Add the water and the remaining broth ingredients. Simmer for 15 minutes.
4. Pour the broth over the spinach and serve.

#### Notes

The source does not specify whether the whitebait is fresh or dried, the cup size or preparation of the dried scallops.

#### Source

Supplied recipe document.

<a id="japanese-stir-fried-lotus-root-and-tau-kwa"></a>

### Japanese stir-fried lotus root and tau kwa

**ID:** `japanese-stir-fried-lotus-root-and-tau-kwa`

**Servings:** 5 portions.

**Time:** Suggested: 10 minutes preparation, 10 minutes steaming and 6 to 8 minutes stir-frying.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 250 g peeled lotus root, sliced about 3 mm thick; use 200 to 350 g
- 200 g tau kwa, patted dry and cut into bite-sized pieces; use 150 to 300 g
- 1 tbsp sesame oil

**Seasoning**

- 1 tbsp mirin
- 1 tbsp sake
- 1 1/2 tbsp soy sauce
- 1 tbsp water

**To finish**

- 1 tsp toasted sesame seeds; use up to 2 tsp
- 1 spring onion, sliced; use up to 2

#### Method

1. Mix the seasoning. Steam the sliced lotus root for about 10 minutes, until tender with a slight crunch, then drain well.
2. Heat the sesame oil in a non-stick frying pan over medium heat. Add the tau kwa and fry for about 3 to 4 minutes, turning to lightly brown the sides.
3. Add the lotus root and stir-fry for 2 minutes. Pour in the seasoning and cook, tossing, for about 1 to 2 minutes until it coats the ingredients and has nearly evaporated.
4. Sprinkle with the toasted sesame seeds and spring onion, then serve.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- The peeled lotus-root and tau-kwa weights replace a root section and one unspecified piece. Choose more root for crunch or more tau kwa for a heartier side dish.
- Garnish amounts and stir-frying times are suggested. Keep the pan over medium heat so the sesame oil and reduced sauce do not scorch.

#### Source

Supplied recipe document.

## Fish and eggs

<a id="japanese-steamed-egg"></a>

### Japanese steamed egg

**ID:** `japanese-steamed-egg`

**Servings:** 5 portions.

**Time:** Start checking after 15 minutes of gentle steaming; the time depends on the depth of the cups.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 4 eggs
- Prepared dashi stock, exactly twice the measured beaten-egg volume
- Dashi sachet, diluted according to its packet to make the required stock volume
- 1 tbsp bonito flakes, to infuse into the stock
- 1 tsp soy sauce
- 1 tsp mirin
- 150 g drained silken tofu, cubed; use 100 to 200 g
- 60 g cooked, shelled edamame; use 50 to 75 g
- 5 cooked crab sticks, each cut into 3 pieces
- Equipment: 5 heatproof cups, each with at least 250 ml capacity, and heatproof lids or foil

#### Method

1. Beat the eggs gently and measure their volume in a jug. Prepare twice that volume of dashi using the sachet's dilution instructions. For example, 200 ml of beaten egg needs 400 ml of prepared dashi.
2. Steep the bonito flakes in the hot dashi, strain, and cool the stock before adding it to the eggs. Measure again after straining and top up with water to the required dashi volume. Do not add salt.
3. Stir the cooled dashi, soy sauce and mirin into the eggs without beating in foam. Strain through a fine sieve.
4. Divide the tofu, edamame and crab sticks among the 5 cups. Pour over the egg mixture, filling each cup no more than four-fifths full. Use an extra cup if necessary; do not overfill.
5. Cover the cups loosely with heatproof lids or foil. Steam gently and start checking after 15 minutes. Continue until the custard is set with a slight wobble and its centre reaches 71°C. Deeper cups take longer.

#### Notes

- Keep 1 part beaten egg to 2 parts prepared dashi by volume. The tofu and edamame ranges change the amount of filling, not this ratio.
- Less filling leaves more custard between the ingredients. The listed cup capacity replaces the undefined bowl size.

#### Source

- [Just One Cookbook: chawanmushi](https://www.justonecookbook.com/chawanmushi-savory-steamed-egg-custard/)

<a id="steamed-egg-minced-meat"></a>

### Steamed egg with minced chicken or pork

**ID:** `steamed-egg-minced-meat`

**Servings:** 5 portions.

**Time:** Steam for 15 minutes; fry meat for 1 to 2 minutes before seasoning, then cook with slurry for 1 to 2 minutes.

**Review:** Imported draft.

#### Ingredients

- 4 eggs
- Water, twice the egg volume
- 150 g silken tofu, sliced, listed as 1 block
- 3 garlic cloves, minced
- 1/2 tsp minced ginger
- 150 g minced chicken or pork
- 1 tbsp soy sauce
- 1/2 tbsp oyster sauce
- 1/2 tsp sugar
- 2 tsp corn starch and 1 tbsp water, for the slurry
- Chopped green onions, for garnish; quantity not specified
- Meat-free seasoning alternative: chicken essence, quantity not specified; 2 tsp soy sauce; 1/2 tsp sugar; 1 tsp sesame oil

#### Method

1. Mix the eggs with water in a 1:2 egg-to-water ratio. Pour over the sliced tofu and steam for 15 minutes.
2. In a pan, fry the garlic and ginger. Add the minced chicken or pork.
3. After 1 to 2 minutes, add the soy sauce, oyster sauce and sugar.
4. When the meat mixture is ready, add the corn starch slurry. Cook for 1 to 2 minutes until the sauce thickens.
5. Pour the meat mixture over the steamed egg. Garnish with chopped green onions.

#### Notes

- The source gives a seasoning alternative without minced meat but no separate method. Chicken essence means this alternative is not vegetarian.

#### Source

- [Instagram recipe reference](https://www.instagram.com/reel/DGKxVhlSeK2/)

<a id="minced-pork-omelette"></a>

### Minced pork omelette

**ID:** `minced-pork-omelette`

**Servings:** 5 portions.

**Time:** Microwave carrot for 1.5 minutes; frying time not specified.

**Review:** Imported draft.

#### Ingredients

- 150 g minced pork
- 6 eggs
- 1/2 carrot, shredded
- A little water, for microwaving the carrot
- 1/2 tsp sesame oil
- 1 tbsp oyster sauce
- 1/2 tsp fish sauce
- 1 tbsp water, for the seasoning
- Oil, for frying; quantity not specified

#### Method

1. Microwave the shredded carrot with a little water for 1.5 minutes.
2. Mix the seasoning with the pork and eggs.
3. Oil a pan and fry the egg mixture.

#### Notes

- The source does not say when to add the carrot or give a cooking time or doneness check for the pork omelette.

#### Source

Supplied recipe document.

<a id="red-onion-omelette"></a>

### Red onion omelette

**ID:** `red-onion-omelette`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 6 eggs
- 1 tsp fish sauce, with the unexplained source qualifier "baby healthy"
- 1/2 red onion, sliced
- 1/2 tsp minced ginger, optional
- Oil, for frying; quantity not specified

#### Method

1. Mix the eggs, fish sauce and onion.
2. Add oil to a hot pan, then add the egg and onion mixture and fry.

#### Notes

- The source does not say when to add the optional ginger or give a frying time.

#### Source

Supplied recipe document.

<a id="otah-egg"></a>

### Otah egg

**ID:** `otah-egg`

**Servings:** 5 portions.

**Time:** Steam for 15 minutes.

**Review:** Imported draft.

#### Ingredients

- 50 g fish, sliced
- 100 g soft tofu, listed as 1/2 packet
- 100 g otah, listed as 1/2 packet
- 2 kaffir lime leaves, finely chopped
- 1 sprig coriander leaves, finely chopped
- 1 egg
- A pinch of salt
- A pinch of sugar
- 3/4 tsp corn flour

#### Method

1. Mash the soft tofu. Combine with the otah, egg, kaffir lime leaves, fish slices and seasoning. Mix well.
2. Steam for 15 minutes.
3. Garnish with chopped coriander.

#### Notes

- The source marks this dish as spicy.

#### Source

Supplied recipe document.

<a id="taiwanese-dan-bing"></a>

### Taiwanese dan bing

**ID:** `taiwanese-dan-bing`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 2 eggs
- 2 Spring Home prata
- 1 sprig spring onion, chopped
- Mozzarella cheese; quantity not specified
- Pork floss; quantity not specified
- Seasoning option 1: 1 tbsp soy sauce, 1/2 tbsp oyster sauce and a drizzle of sesame oil
- Seasoning option 2: 3 tbsp light soy sauce, 3 tbsp dark soy sauce, 1/4 cup water, 2 tbsp mirin, 1 tsp brown sugar, 1 tsp Chinese black vinegar, 1/8 tsp garlic granules, 1/8 tsp coarse sea salt and a small pinch of five-spice powder
- Corn starch slurry, for seasoning option 2; quantity not specified

#### Method

1. For seasoning option 2, boil the sauce ingredients and thicken with corn starch slurry.
2. Pan-fry the prata until light and fluffy. Set aside.
3. Pan-fry the egg. Add cooked prata and cheese before folding it over.

#### Notes

- Choose one of the two seasoning options. The source does not specify when to add the sauce, spring onion or pork floss.
- The water for seasoning option 2 is listed as both 1/4 cup and 4 tbsp.

#### Source

- [I Heart Umami: dan bing](https://iheartumami.com/dan-bing-taiwanese-breakfast-crepes/)
- [I Heart Umami: Taiwanese thick soy sauce](https://iheartumami.com/taiwanese-thick-soy-sauce/#wprm-recipe-container-60346)

<a id="miso-mushroom-fish"></a>

### Miso mushroom fish

**ID:** `miso-mushroom-fish`

**Servings:** 5 portions.

**Time:** About 20 to 25 minutes, including 9 to 12 minutes of steaming; check the fish rather than relying on time alone.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 250 g boneless cod fillet, or boneless halibut fillet
- 75 g fresh shimeji mushrooms, weighed after trimming the base; use 50 to 100 g
- 10 g fresh ginger, thinly sliced; use 5 to 15 g to taste
- 1/2 tbsp soy sauce
- 1 tbsp mirin
- 1 tbsp white miso paste
- 1 tsp butter
- 2 tbsp water

#### Method

1. Bring a steamer to a steady steam. Mix the soy sauce, mirin, miso and water until the miso dissolves. Separate the trimmed shimeji into small clusters.
2. Place the fish on a large sheet of baking paper set on a heatproof plate. Arrange the mushrooms and ginger around and over it, pour over the sauce and dot with the butter. Fold the paper into a loose parcel that holds the sauce.
3. Steam for 9 to 12 minutes. Open the parcel carefully and check the thickest part of the fish; continue steaming until it reaches 63°C and the mushrooms are tender.
4. Serve the fish, mushrooms and sauce together.

#### Notes

- Cod is the suggested fish for this adaptation; halibut is an alternative. The original notes did not name the fish.
- The 75 g shimeji default is a suggested trimmed fresh weight, not a conversion of the unknown half-packet. Use the upper end for more mushrooms without changing the sauce.
- The original 250 g fish amount is preserved as a shared dish for 5 portions.

#### Source

Supplied recipe document.

<a id="steamed-pomfret"></a>

### Steamed pomfret

**ID:** `steamed-pomfret`

**Servings:** 5 portions.

**Time:** Suggested: 10 minutes preparation and about 10 to 15 minutes steaming; check doneness rather than relying on time.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 1 whole cleaned pomfret, about 500 g after cleaning; use 400 to 700 g
- 1 tbsp wolfberries, rinsed
- 70 ml unsalted chicken essence; use 60 to 80 ml
- 15 g ginger, thinly sliced; use 10 to 20 g
- 1 tsp fish soy sauce, optional

#### Method

1. Pat the cleaned pomfret dry and score its thickest flesh with two shallow cuts on each side. Place half the ginger in a deep heatproof plate and set the fish on top.
2. Scatter over the wolfberries and remaining ginger. Pour over the chicken essence and optional fish soy sauce. No separate marinating step is needed in this adaptation.
3. Steam over steadily simmering water, covered. Start checking after 10 minutes and continue until the thickest flesh, away from the bone, reaches 63°C. A larger fish may take longer than 15 minutes.
4. Serve the fish with its cooking juices and remove bones when portioning.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- The cleaned-fish weight, chicken-essence volume and ginger amount are suggested working quantities. Bottle sizes vary, so measure the essence instead of assuming one bottle is 70 ml.
- The fish is a shared dish for five, not five whole fish. Scale from the cleaned weight and allow for bones.

#### Source

Supplied recipe document.

<a id="steamed-dory-fillet"></a>

### Steamed dory fillet

**ID:** `steamed-dory-fillet`

**Servings:** 5 portions.

**Time:** Start checking the fish after 8 minutes of steaming; make the sauce while it steams.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 500 g dory fillet
- 2 sprigs spring onion, white parts chopped and green parts reserved
- 6 slices ginger
- 2 tbsp minced garlic
- 2 tsp cooking oil, for sauteing
- 1 small pinch salt, optional after tasting
- 2 tbsp soy sauce
- 3 tbsp hot water
- 1 tbsp oyster sauce
- 1 tbsp sesame oil
- 1 tsp sugar
- 1/8 tsp white pepper; adjust to taste

#### Method

1. Bring the steamer to a steady steam. Pat the fish dry and place it on the spring onion whites and ginger in a heatproof plate. Steam and start checking after 8 minutes; continue until the thickest part reaches 63°C.
2. Mix the soy sauce, hot water, oyster sauce, sesame oil, sugar and white pepper in a bowl.
3. Heat the cooking oil over medium-low heat. Saute the garlic until fragrant and lightly golden, then stir in the sauce. Heat through and taste before adding the optional pinch of salt.
4. Drain any excess steaming liquid from the plate if desired. Pour the hot garlic sauce over the fish and finish with the reserved spring onion greens.

#### Notes

- The frying oil and pepper amounts are suggested starting quantities. The sauce is already salty, so add the optional salt only after tasting.

#### Source

Supplied recipe document.

<a id="honey-baked-miso-halibut"></a>

### Maple-baked miso halibut

**ID:** `honey-baked-miso-halibut`

**Servings:** 5 portions.

**Time:** Marinate for 2 hours in the fridge; bake for 6 minutes, then broil briefly as needed while checking doneness.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 400 g halibut
- 2 tbsp miso
- 1 tbsp mirin
- 1 tbsp maple syrup
- 3/4 tbsp sesame oil
- 1/8 tsp black pepper; adjust to taste

#### Method

1. Marinate the halibut with the miso, mirin, maple syrup, sesame oil and black pepper for 2 hours in the fridge.
2. Preheat the oven to 180°C. Remove the fish from the fridge while the oven heats, for no more than the source's 15-minute standing time. Place on a foil-lined, broiler-safe metal tray and bake for 6 minutes.
3. Switch to the oven's top heat and watch closely until the surface colours. The source suggests up to 8 minutes, but the glaze can burn sooner. If it colours before the fish is cooked, return to 180°C baking and cover loosely with foil.
4. Finish cooking until the thickest part of the fish reaches 63°C. Use temperature and glaze colour rather than the combined source times alone.

#### Notes

- The title now matches the maple syrup ingredient. The stable recipe ID is retained so existing links continue to work.
- The source's bake and broil times are starting guidance, not a guarantee for every fillet thickness or oven.

#### Source

Supplied recipe document.

<a id="steamed-halibut-garlic-ginger"></a>

### Steamed halibut with garlic and ginger sauce

**ID:** `steamed-halibut-garlic-ginger`

**Servings:** 5 portions.

**Time:** About 25 minutes for either option. For option 1, start checking after 10 minutes of steaming; for option 2, start checking after 6 minutes.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

**Option 1: sesame paste, garlic and ginger**

- 400 g boneless halibut, in 2 pieces; use 300 to 500 g
- 1 tsp unsweetened Chinese toasted sesame paste mixed with 2 tsp water, for coating the fish
- 2 slices ginger and 1 tbsp rinsed wolfberries, for steaming
- Sauce: 1 tsp oyster sauce, 1 tsp soy sauce, 1 tsp mirin and 1 tbsp water
- Aromatics: 2 tbsp ginger sticks, 5 garlic cloves, minced, and 4 spring onions, sliced with whites and greens separated
- 2 tsp neutral cooking oil, for frying the aromatics

**Option 2: ginger and soy sauce**

- 250 g halibut or cod
- 2 tbsp shredded ginger
- Sauce: 1.5 tsp soy sauce, 1.5 tsp Chinese wine, 1 tsp water and 1 tsp sesame oil
- 1 spring onion, sliced, for serving; use 1 to 2 to taste

#### Method

**Option 1**

1. Bring the steamer to a steady steam. Mix the sesame paste with its 2 tsp water and spread over the halibut. Place the ginger slices on a heatproof plate, set the fish on top and scatter over the wolfberries.
2. Steam for 10 to 15 minutes. Check the thickest part after 10 minutes and continue until it reaches 63°C; thicker pieces may take longer.
3. While the fish steams, mix the option 1 sauce ingredients. Heat the neutral oil in a small pan over medium heat. Fry the ginger sticks, garlic and spring onion whites for about 1 minute, until fragrant but not browned. Add the sauce and simmer for 30 seconds.
4. Spoon the hot aromatics and sauce over the cooked fish. Scatter over the spring onion greens and serve with the steaming juices.

**Option 2**

1. Bring the steamer to a steady steam and place its 250 g fish with the shredded ginger on a heatproof plate.
2. Steam and start checking after 6 minutes. Continue until the thickest part of the fish reaches 63°C; timing depends on its thickness.
3. While the fish steams, combine the option 2 sauce ingredients in a small pan and bring to a gentle simmer.
4. Pour the hot sauce over the cooked fish and scatter over the sliced spring onion.

#### Notes

- Choose one option and use only that option's ingredients for the shopping list.
- Option 1 is a proposed complete version. It uses unsweetened Chinese toasted sesame paste thinned with water for the source's unidentified "sesame sauce". This is an explicit substitution, not a claim about what the original author used. The cooking oil, added water and steaming guidance are also suggested additions.
- Use 400 g fish by default for option 1, or the lower or upper amount to suit the other dishes and appetite. Option 2 keeps the original 250 g fish amount. Both are shared dishes for 5 portions, rather than five individual main courses.

#### Source

Supplied recipe document.

<a id="tomato-egg"></a>

### Tomato egg

**ID:** `tomato-egg`

**Servings:** 5 portions.

**Time:** Fry garlic and onion for about 15 seconds; cook tomatoes for 1 to 2 minutes, then finish cooking the eggs.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 5 large eggs
- 1 small pinch salt and 1 small pinch white or black pepper, for the eggs
- 3 garlic cloves, minced
- 1 green onion, chopped, with white and green parts kept separate
- 2 medium tomatoes, each cut into 8 wedges
- 2 tbsp ketchup
- 1 tbsp oyster sauce
- 1 tsp wolfberries, soaked and mashed
- 1/3 cup water
- 1 tsp sesame oil
- 2 tbsp oil, divided, for frying

#### Method

1. Beat the eggs with the salt and pepper. Heat 1 tbsp oil in a wok over medium-high heat, add the eggs and stir until softly set. Transfer them to a clean plate and wipe out the pan.
2. Add the remaining 1 tbsp oil. Fry the garlic and white parts of the green onion until fragrant, about 15 seconds.
3. Add the tomatoes, ketchup, oyster sauce, wolfberries and water. Cook for 1 to 2 minutes until the tomatoes soften.
4. Return the eggs to the wok and stir in the sesame oil. Cook until the egg mixture reaches 71°C, then garnish with the green parts of the onion.

#### Notes

- Beat the single pinch of salt and pepper into the eggs; do not add a second salt portion. This resolves the duplicate salt wording.

#### Source

- [Cookerru: tomato egg](https://www.cookerru.com/tomato-egg/)

<a id="fried-egg-shallots-spring-onion"></a>

### Fried egg with shallots and spring onion

**ID:** `fried-egg-shallots-spring-onion`

**Servings:** 5 portions.

**Time:** Fry the eggs until set, then return them to the pan to finish in the sauce.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 5 eggs
- 1/2 tsp fish sauce
- 1/2 tsp sesame oil
- 1.5 large shallots, thinly sliced
- 2 sprigs spring onion, chopped, with whites and greens separated
- 1 tbsp oyster sauce
- 2 tsp cooking oil, divided; use up to 1 tbsp if the pan needs it

#### Method

1. Beat the eggs with the fish sauce and sesame oil. Heat 1 tsp cooking oil in a nonstick pan, add the eggs and fry until set in soft pieces. Transfer to a clean plate.
2. Add the remaining cooking oil. Fry the shallots and spring onion whites until softened, then stir in the oyster sauce.
3. Return the eggs to the pan. Toss gently until coated and heated through, with the egg mixture reaching 71°C. Fold in the spring onion greens and serve.

#### Notes

- Large shallots follow the ingredient list. The source title referred to big onion.
- Returning the eggs after the oyster sauce completes the original method. The frying oil is a suggested quantity.

#### Source

- [Instagram recipe reference](https://www.instagram.com/reel/DDf2XkmyrZi/)

<a id="baked-tomato-fish-foil"></a>

### Baked tomato fish in foil

**ID:** `baked-tomato-fish-foil`

**Servings:** 5 portions.

**Time:** Stir-fry for about 2 minutes; steam vegetables for about 6 minutes; start checking the fish after 15 minutes of baking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 200 g firm white fish, such as threadfin or cod
- 1.5 tsp olive oil
- 1.5 tsp garlic, chopped
- 1/2 medium onion, chopped
- 1/2 tsp Italian seasoning; use 1/4 to 3/4 tsp to taste
- 2 tbsp tomato paste
- 2 tomatoes, diced
- 1/2 medium zucchini, cut into matchsticks
- 300 g peeled, deseeded pumpkin or squash, cut into thin matchsticks; use 200 to 400 g
- 1/2 bell pepper, cut into matchsticks, optional
- 1/8 tsp black pepper; adjust to taste
- 1 small pinch salt, optional after tasting

#### Method

1. Heat the olive oil and stir-fry the onion and garlic for about 2 minutes. Add the Italian seasoning, black pepper, tomato paste and diced tomatoes. Simmer until the sauce thickens, then taste and add the optional salt if needed.
2. Steam the zucchini, pumpkin and optional bell pepper for about 6 minutes, until nearly tender. Thicker pieces may need longer.
3. Preheat the oven to 180°C. Arrange the vegetables evenly on foil on a baking tray, place the fish on top and pour over the sauce. Fold the foil into a closed pouch.
4. Bake and start checking after 15 minutes. Continue until the fish reaches 63°C and the vegetables are tender. Open the pouch carefully to release the steam.

#### Notes

- The seasoning and pumpkin weights are suggested quantities. The pumpkin range replaces the variable instruction to use half a pumpkin.
- The original 200 g fish quantity is preserved for 5 shared portions; serve it with other dishes if more food is needed.
- The linked recipe is a reference only.

#### Source

- [Tuttorosso: baked fish in foil packets](https://tuttorossotomatoes.com/recipes/detail/baked-fish-in-foil-packets)

<a id="baked-salmon-teriyaki"></a>

### Baked salmon with teriyaki sauce

**ID:** `baked-salmon-teriyaki`

**Servings:** 5 portions.

**Time:** Marinate for 1 hour in the fridge; start checking the fish after 10 minutes of baking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 600 g salmon, about 3 pieces
- 1 knob ginger, cut into strips
- 1.5 tsp sesame oil
- 1.5 tbsp sake
- 1.5 tbsp mirin
- 2.5 tbsp soy sauce
- 1 tbsp honey or 1/2 tbsp brown sugar

#### Method

1. Marinate the fish with the sesame oil, sake, mirin, soy sauce and honey or brown sugar for 1 hour in the fridge.
2. Preheat the oven to 180°C. Put the fish on baking paper, arrange the ginger strips over it and fold the paper into a closed parcel on a baking tray.
3. Bake and start checking after 10 minutes. Continue until the thickest part of the fish reaches 63°C; thicker pieces take longer. Open the parcel carefully to release the steam.

#### Notes

- Adding the ginger before baking completes the original method. The 10-minute source timing is a first check, not a guarantee of doneness.

#### Source

Supplied recipe document.

<a id="ginger-soy-baked-salmon"></a>

### Ginger soy fish with baked salmon

**ID:** `ginger-soy-baked-salmon`

**Servings:** 5 portions.

**Time:** Bake at 180°C and start checking after 10 minutes; prepare the ginger and sauce while the oven heats.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 600 g salmon, about 3 pieces
- 1 knob ginger, cut into strips
- 2 tbsp sesame oil, for frying the ginger
- 1 tbsp of the ginger frying oil, reserved to season the salmon; not additional oil
- 1 tbsp soy sauce
- 3 tbsp cold water
- 1/2 tsp cornstarch
- 1 tsp honey

#### Method

1. Preheat the oven to 180°C. Gently fry the ginger strips in the sesame oil until fragrant and lightly golden. Lift out the ginger and reserve it, then measure 1 tbsp of the frying oil for the fish.
2. Brush the salmon with the reserved 1 tbsp ginger oil and place it on a lined baking tray. Bake and start checking after 10 minutes. Continue until the thickest part reaches 63°C.
3. Mix the soy sauce, cold water, cornstarch and honey until smooth. Pour into a small pan and heat gently, stirring, until the sauce simmers and lightly thickens.
4. Serve the fish with the sauce offered separately and the fried ginger scattered over it.

#### Notes

- Keep the sauce separate until serving. The source says it is thick and salty and should not be doubled automatically.
- Baking is an adaptation to complete the supplied salmon version. The linked recipe uses pan-fried white fish. The suggested first-check time depends on fillet thickness.
- The reserved tablespoon of ginger oil is taken from the 2 tbsp used for frying, so the shopping list needs 2 tbsp sesame oil in total.

#### Source

- [Rasa Malaysia: ginger soy fish](https://rasamalaysia.com/ginger-soy-fish/)

<a id="japanese-creamy-fish-stew"></a>

### Japanese creamy fish stew

**ID:** `japanese-creamy-fish-stew`

**Servings:** 5 portions.

**Time:** Simmer the vegetables until tender, then cook the fish gently in the finished sauce. Total time depends on the size of the pieces.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 5 garlic cloves, minced
- 150 g brown mushrooms, sliced; use 100 to 200 g
- 2.5 tbsp unsalted butter
- 2.5 tbsp plain flour
- 180 ml vegetable cooking water or prepared stock
- Optional dashi or chicken stock powder: follow the label to make 180 ml stock, only if not using prepared stock
- 180 ml milk or cream; choose one
- 4 baby potatoes, quartered
- 2 carrots, cut into bite-sized pieces
- 1 stalk leek, cleaned and sliced
- 1 onion, cut into bite-sized pieces
- Water to cover the vegetables for boiling
- 550 g dory, cod or barramundi fillets, about 2 to 3 fillets; use 500 to 600 g total, cut into bite-sized pieces

#### Method

1. Put the potatoes, carrots, onion and leek in a pot and add enough water to cover them. Simmer until tender, then drain, reserving at least 180 ml of the cooking water.
2. In another pan, melt the butter over medium-low heat. Cook the garlic and mushrooms until softened. Stir in the flour and cook for about 1 minute, stirring so it does not brown.
3. If using the optional stock powder, dissolve the label-directed amount in 180 ml reserved vegetable water. Gradually stir this, plain vegetable water or prepared stock into the flour mixture until smooth; use 180 ml liquid in total. Add the cooked vegetables.
4. Stir in the milk or cream and bring to a gentle simmer, stirring to prevent sticking.
5. Add the fish pieces. Simmer gently until the fish reaches 63°C in the thickest pieces, stirring carefully so they stay intact. Add reserved vegetable water 1 tbsp at a time if the sauce is too thick, then taste before adding any extra seasoning.

#### Notes

- Milk and cream are alternatives. Milk makes a lighter sauce; cream makes it richer.
- The original powder note gave 1 tbsp without a reliable dilution. Use the product label for 180 ml prepared stock; do not add stock powder to already prepared stock.
- The mushroom weight and fish-cooking step are practical adaptations. The extra vegetable water is used only to adjust sauce thickness.

#### Source

- [Instagram recipe reference](https://www.instagram.com/reel/Cr0IXI5gY-J/)

<a id="sweet-sour-fried-tofu-fish"></a>

### Sweet and sour fried tofu

**ID:** `sweet-sour-fried-tofu-fish`

**Servings:** 5 portions.

**Time:** Fry the tofu until crisp; cook the vegetables until softened and simmer the sauce until it coats a spoon.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 300 g firm tofu, drained and cubed; use 250 to 400 g, or the same weight of egg tofu cut into thick slices
- 2 tbsp cornstarch, for coating; use 1 to 3 tbsp as needed for a thin coating
- 1 small pinch each of mushroom salt and garlic powder
- 3 tbsp cooking oil, divided; use 2 to 4 tbsp as needed for shallow frying and the vegetables
- 50 g pineapple, cut into pieces; use 30 to 60 g
- 1 shallot or 1/2 small onion, cut into pieces
- 1/2 capsicum, cut into pieces
- 1 tbsp pineapple juice
- 2.5 tbsp ketchup
- 1 tbsp soy sauce
- 1/2 tbsp oyster sauce
- 1 tsp sugar or honey
- 1 tbsp apple cider vinegar
- 1.5 tbsp water
- Slurry: 1 tsp cornstarch mixed with 1 tbsp cold water

#### Method

1. Pat the tofu dry. Coat it lightly with the coating cornstarch, mushroom salt and garlic powder. Heat about 2 tbsp oil and shallow-fry the tofu, turning gently, until crisp. Set aside.
2. Mix the pineapple juice, ketchup, soy sauce, oyster sauce, sugar or honey, vinegar and 1.5 tbsp water in a bowl. Mix the slurry separately.
3. Add about 1 tbsp oil to the pan if needed. Stir-fry the onion, capsicum and pineapple until softened.
4. Add the sauce mixture and bring it to a gentle simmer. Stir the slurry again, add half, and simmer while stirring until the sauce thickens. Add more slurry only if needed to lightly coat a spoon.
5. Pour the sauce and vegetables over the tofu just before serving to keep the coating crisp.

#### Notes

- More pineapple makes the dish sweeter and fruitier. Use more tofu for a larger share of the meal; the dish still uses a 5-portion base.
- The original box or tube counts are replaced by suggested tofu weights. Choose one tofu type.
- The source title offered fish without a fish quantity or method. This adaptation covers tofu only; the stable recipe ID is retained.

#### Source

Supplied recipe document.

## Chicken, pork and beef

<a id="steamed-tofu-egg-pork"></a>

### Steamed tofu and egg with pork

**ID:** `steamed-tofu-egg-pork`

**Servings:** 5 portions.

**Time:** Suggested: 10 minutes preparation and about 15 to 20 minutes gentle steaming.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 300 g silken tofu, drained and sliced; use 250 to 350 g
- 2 eggs, beaten
- 120 ml chicken broth, cooled
- 100 g minced pork
- 1/2 tsp sesame oil, for the pork
- 1/2 tsp cornflour, for the pork

**Sauce**

- 1 tsp soy sauce
- 1 tsp oyster sauce
- 1 tbsp water
- 1/2 tsp sesame oil
- 1/2 tsp sugar

#### Method

1. Mix the minced pork with its sesame oil and cornflour. Break it into small loose pieces rather than one thick mound. No resting time is required in this adaptation.
2. Mix the beaten eggs with the cooled chicken broth. Place the sliced tofu in a shallow heatproof dish, pour the egg mixture through a sieve over the tofu, then scatter the pork evenly over it. Keep the layer about 3 cm deep or less; use two dishes if necessary.
3. Cover loosely with foil or a heatproof lid. Steam gently and start checking after 15 minutes. Continue until the custard is set and the egg mixture and pork reach 71°C throughout. A deeper dish takes longer.
4. Mix all sauce ingredients in a small saucepan. Heat gently while stirring until the sugar dissolves and the sauce is hot. Drizzle over the cooked tofu and egg before serving.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- The tofu weight replaces the unknown box size. More tofu adds filling without changing the recorded two eggs and 120 ml broth.
- The cornflour amount, broth-mixing step and heated sauce preparation are suggested completions. The original fixed 8-minute steam is replaced by a doneness check suitable for the dish's depth.

#### Source

- [Instagram recipe reference](https://www.instagram.com/reel/Ce0qJfyNsPl/)

<a id="miso-mapo-tofu"></a>

### Miso mapo tofu

**ID:** `miso-mapo-tofu`

**Servings:** 5 portions.

**Time:** Fry the chicken until cooked through, then simmer with the tofu for about 2 minutes before thickening.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 250 g silken tofu, cubed
- 100 g minced chicken
- 1 tsp sesame oil and 1 tsp cornstarch, for the chicken marinade
- 1 spring onion, chopped
- 1 garlic clove, minced
- 1/2 tsp minced ginger
- 1 tsp cooking oil, for frying
- 1 tbsp sake, optional
- 1 tbsp mirin
- 300 ml water
- 1 tbsp miso
- 1/2 tsp sesame oil, to finish; use 1/4 to 1/2 tsp to taste
- Slurry: 1 tsp cornstarch mixed with 1 tbsp cold water

#### Method

1. Mix the minced chicken with the marinade sesame oil and cornstarch while preparing the other ingredients. Dissolve the miso in the 300 ml water in a separate bowl.
2. Heat the cooking oil. Fry the ginger and garlic until fragrant, then add the chicken and break it into small pieces. Continue cooking until the chicken reaches 74°C.
3. Add the optional sake, mirin, miso-water mixture and tofu. Simmer gently for about 2 minutes, stirring carefully to avoid breaking the tofu.
4. Stir the slurry again and add half. Simmer and stir until the sauce thickens; add more slurry if needed for a light coating consistency.
5. Stir in the finishing sesame oil and serve with the spring onion.

#### Notes

- Use minced chicken throughout, following the ingredient list. The source's conflicting pork reference is resolved.
- The frying oil, finishing oil and slurry are suggested measured quantities. The marinade cornstarch and slurry cornstarch are separate amounts, 2 tsp in total if all the slurry is used.

#### Source

Supplied recipe document.

<a id="steamed-chicken-mushrooms-black-fungus"></a>

### Steamed chicken with mushrooms and black fungus

**ID:** `steamed-chicken-mushrooms-black-fungus`

**Servings:** 5 portions.

**Time:** About 60 minutes, including at least 30 minutes to marinate while the dried ingredients soak, then 15 to 20 minutes to steam.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 3 small boneless chicken thighs, cut into 2 cm cubes
- 4 red dates, halved and pitted
- 10 g dried black fungus; use 5 to 15 g for less or more fungus
- 3 dried shiitake mushrooms
- 1 tbsp wolfberries, rinsed
- 20 g cooked bak kwa, thinly sliced, optional; use 10 to 30 g if included
- 1 tbsp oyster sauce
- 1 tbsp light soy sauce
- 1 tsp sesame oil
- 1 tsp cornflour
- 1/2 tsp minced ginger
- 1/8 tsp white pepper
- 1 spring onion, chopped, for serving
- 5 g coriander, chopped, optional; use 3 to 10 g if included
- Water to cover the dried fungus and mushrooms in separate bowls, for soaking only

#### Method

1. Mix the chicken with the oyster sauce, light soy sauce, sesame oil, cornflour, ginger and white pepper. Cover and refrigerate for at least 30 minutes.
2. Rinse the dried fungus and mushrooms. Soak them in separate bowls of warm water until fully softened, usually 20 to 30 minutes for the fungus and 30 minutes for the mushrooms; follow any longer package instructions in the refrigerator. Drain both and discard the water. Trim the fungus's tough bases and tear it into bite-size pieces. Remove the mushroom stems and slice the caps thinly.
3. Bring a steamer to a steady steam. Combine the marinated chicken, fungus, mushrooms, dates, wolfberries and optional bak kwa on a shallow heatproof plate. Spread into an even layer.
4. Steam for 15 to 20 minutes. Check a thick chicken cube and continue until its centre reaches 74°C. Keep the steamer supplied with water.
5. Scatter over the spring onion and optional coriander. Serve with the cooking juices.

#### Notes

- The dried fungus weight replaces the unknown half-packet with a suggested amount. It is not a conversion of the original packet. The optional bak kwa and garnish amounts are also suggested.
- Boneless thighs are specified for the cubed chicken method. These amounts make a shared dish for 5 portions.
- Soak dried fungus only until softened and cook it promptly. If soaking will take more than 2 hours, keep it in the refrigerator. See the [Hong Kong Consumer Council's preparation guidance](https://www.consumer.org.hk/en/press-release/p-556-dried-edible-fungi).

#### Source

Supplied recipe document.

<a id="braised-chicken-mushrooms-tau-kwa"></a>

### Braised chicken with mushrooms and tau kwa

**ID:** `braised-chicken-mushrooms-tau-kwa`

**Servings:** 5 portions.

**Time:** About 80 to 90 minutes, including 30 minutes to soak the mushrooms and 40 minutes to braise. Boil the eggs while the mushrooms soak if needed.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 400 g boneless chicken thigh, cut into 3 cm pieces
- 5 g dried black fungus; use 5 to 10 g for more fungus
- 300 g firm tofu, also called tau kwa, cut into 2 cm pieces; use 200 to 400 g
- 8 dried shiitake mushrooms
- 5 hard-boiled eggs, peeled
- 15 g ginger, sliced; use 10 to 20 g to taste
- 2 scallions, halved
- 2 garlic cloves, smashed
- 2 bay leaves
- 2 star anise
- 1 cinnamon stick
- 1 tsp whole cloves
- 1 tbsp neutral cooking oil
- 1.5 tsp oyster sauce
- 1.5 tsp sesame oil
- 1 tbsp light soy sauce
- 1 tbsp dark soy sauce
- 1 tbsp rock sugar
- 1 tsp fish sauce
- 2 tbsp Shaoxing wine
- 400 ml strained mushroom soaking liquid and water combined, plus up to 200 ml hot water if needed to keep the chicken mostly covered
- 900 g cooked rice, for serving; use 650 to 1000 g according to appetite, or 300 g dried noodles, using 250 to 350 g instead of rice
- Water to cover the fungus and mushrooms in separate bowls for soaking

#### Method

1. Rinse the mushrooms and soak them in warm water for about 30 minutes, until fully softened. Strain the soaking liquid through a fine sieve and measure 400 ml, topping up with water as needed. Remove the mushroom stems and halve the caps. Separately soak the fungus in water for 20 to 30 minutes, or as directed on its packet, until fully softened. Drain and discard its water, trim the tough bases and tear into bite-size pieces.
2. If starting with raw eggs, cover them with water in a saucepan. Bring to a gentle boil and cook for 10 to 12 minutes, until the yolks and whites are firm. Cool briefly in cold water and peel.
3. Heat the neutral oil in a snug casserole over medium heat. Brown the tau kwa for 3 to 4 minutes, turning it carefully, then lift it out. Fry the ginger, garlic and scallions for 1 minute. Add the chicken and fry for 3 minutes.
4. Add the measured 400 ml liquid, mushrooms, bay leaves, star anise, cinnamon, cloves, oyster sauce, sesame oil, both soy sauces, rock sugar, fish sauce and Shaoxing wine. Bring to a simmer, cover and cook gently for 30 minutes. Stir occasionally and add some of the extra hot water if needed to keep the chicken mostly covered.
5. Add the tau kwa, peeled boiled eggs and softened fungus. Turn the eggs in the sauce, cover and simmer for another 10 minutes. Check that the chicken reaches 74°C and the mushrooms and fungus are tender.
6. Remove the bay leaves, star anise, cinnamon and any visible whole cloves. Serve with the measured cooked rice or noodles cooked according to their packet instructions.

#### Notes

- This adaptation uses the source's 400 g weight as boneless chicken thigh. The separate source count of 2 thighs and 4 drumlets is not treated as an equivalent weight and is not an additional amount to buy.
- The dried fungus and tau kwa weights, ginger amount, cooking oil, serving quantities and extra-water allowance are suggested amounts. They do not convert the original half-cup of fungus or two pieces of tau kwa.
- The mushrooms cook in the braising liquid; they do not need a separate boiling step. Add the already boiled eggs and soaked fungus for the final 10 minutes.
- Soak dried fungus only until softened. If soaking will take more than 2 hours, refrigerate it; see the [Hong Kong Consumer Council's preparation guidance](https://www.consumer.org.hk/en/press-release/p-556-dried-edible-fungi).

#### Source

Supplied recipe document.

<a id="soya-chicken-potato-stew"></a>

### Soya chicken and potato stew

**ID:** `soya-chicken-potato-stew`

**Servings:** 5 portions.

**Time:** Simmer for about 30 minutes; add optional sweet potato for the final 10 to 15 minutes.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 2 small potatoes, cut into bite-sized pieces
- 1 small sweet potato, optional, cut into bite-sized pieces
- 2 carrots, cut into bite-sized pieces
- 800 g chicken, chopped into bite-sized pieces
- 5 garlic cloves, lightly crushed
- 1 tbsp cooking oil; use 2 tsp to 1 tbsp according to the pan
- 1 tbsp light soy sauce
- 400 ml water
- 1 tbsp dark soy sauce
- 1 tbsp wolfberries
- 1 tsp rock sugar, optional; omit when using sweet potato
- 1 tbsp sesame oil

#### Method

1. Heat the cooking oil in a wok and saute the garlic until golden brown.
2. Add the chicken and stir-fry until the outside turns white; this does not mean it is cooked through.
3. Add the carrots and potatoes and stir-fry to combine. Add the light soy sauce and mix well.
4. Add the water, dark soy sauce, wolfberries and optional rock sugar. Stir briefly, cover and simmer for about 30 minutes, until the vegetables are tender and the chicken reaches 74°C in the thickest pieces.
5. If using sweet potato, omit the sugar and add the sweet potato only for the final 10 to 15 minutes so it does not turn mushy.
6. Stir in the sesame oil. If the stew begins to dry out before it is cooked, add hot water a little at a time.

#### Notes

- Add the optional sugar with the braising liquid. Omit it when using sweet potato, as directed in the source.
- The frying oil is a suggested measured amount.

#### Source

- [The Hungry Excavator: soya chicken and potato stew](http://www.thehungryexcavator.com/2012/11/soya-chicken-and-potato-stew-recipe.html)

<a id="baked-honey-soy-chicken"></a>

### Baked honey soy chicken

**ID:** `baked-honey-soy-chicken`

**Servings:** 5 portions.

**Time:** Marinate for 30 minutes; bake for 35 minutes, then another 5 to 10 minutes.

**Review:** Imported draft.

#### Ingredients

- 1,000 g chicken thighs or wings
- 2 tbsp oyster sauce
- 2 tbsp soy sauce
- 1 tbsp water
- 1 tbsp sesame oil
- 1.5 tbsp sake
- 8 cm ginger, peeled and cut into strips
- 6 cloves garlic, peeled and minced
- 1 tbsp honey, for glazing

#### Method

1. Mix the chicken with the marinade ingredients and set aside for 30 minutes. Reserve the honey for glazing.
2. Preheat the oven to 190°C.
3. Wrap and seal the chicken in cooking paper or foil. Bake for 35 minutes.
4. Open the paper or foil, glaze with honey and bake for another 5 to 10 minutes to brown the chicken.

#### Source

Supplied recipe document.

<a id="potatoes-carrots-minced-meat"></a>

### Potatoes and carrots with minced meat

**ID:** `potatoes-carrots-minced-meat`

**Servings:** 5 portions.

**Time:** About 35 to 45 minutes, including 10 minutes to marinate and 15 to 20 minutes to simmer.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 5 garlic cloves, minced
- 1 spring onion, sliced, white and green parts separated
- 200 g minced chicken or pork
- 1.5 tsp cornflour and 1 tsp soy sauce, for the meat marinade
- 2 medium carrots, cut into 1 cm cubes
- 5 baby potatoes, cut into 1 cm cubes
- 1.5 medium onions, cubed
- 1 tbsp neutral cooking oil
- 1 tbsp oyster sauce
- 1 tbsp dark soy sauce
- 1 tsp soy sauce, for the seasoning
- 400 ml water; use 300 to 500 ml, enough to just cover the ingredients in a snug pan
- Slurry: 2 tsp cornflour mixed with 2 tbsp cold water

#### Method

1. Mix the minced meat with its 1.5 tsp cornflour and 1 tsp soy sauce. Refrigerate for 10 minutes while preparing the vegetables.
2. Heat the oil in a deep frying pan or small saucepan over medium heat. Fry the onion, garlic and spring onion whites for 2 minutes. Add the minced meat and stir-fry for 3 to 4 minutes, breaking up any clumps.
3. Add the carrots and potatoes and stir for 2 minutes. Add the oyster sauce, dark soy sauce, seasoning soy sauce and enough of the measured water to just cover the ingredients. Bring to a simmer.
4. Partly cover and simmer for 15 to 20 minutes, until a fork enters the potatoes and carrots easily. Stir occasionally; add the remaining measured water if the pan becomes dry. Check that minced chicken reaches 74°C or minced pork reaches 71°C.
5. Stir the slurry again, then add half to the simmering sauce. Cook for 1 minute. Add more slurry only if needed and simmer for another minute, until the sauce lightly coats the ingredients. Scatter over the spring onion greens and serve.

#### Notes

- The source also calls this dish "ABC".
- The cooking oil, water range, slurry and timings are suggested additions. Start with half the slurry because potato starch and evaporation also thicken the sauce. The full slurry is a measured starting quantity, not an instruction to add it all.

#### Source

- [YouTube recipe reference](https://youtu.be/ZZXg7FYuiLI)

<a id="beef-pork-tomato-stew"></a>

### Beef or pork tomato stew

**ID:** `beef-pork-tomato-stew`

**Servings:** 5 portions.

**Time:** About 2 to 3.5 hours. Pork collar usually softens sooner than beef chuck or brisket; use tenderness as the endpoint.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 1 medium onion, thickly sliced
- 1.5 medium carrots, cut into 2 cm pieces
- 4 medium potatoes, peeled and cut into 3 cm pieces
- 600 g beef chuck, beef brisket or pork collar, cut into 3 cm cubes; use 500 to 700 g according to appetite
- 500 ml water, plus 100 to 300 ml hot water if needed during simmering
- 1 sprig fresh basil, leaves torn and stalk discarded
- 1 tsp dried Italian herbs
- 2 tomatoes, skins removed and flesh cubed
- 1 tbsp butter
- 500 g tomato-based pasta sauce; use 400 to 600 g for a lighter or stronger tomato flavour
- 30 g raisins; use 20 to 50 g for less or more sweetness

#### Method

1. Melt the butter in a heavy pot over medium heat. Pat the meat dry and brown it in two batches for 3 to 5 minutes per batch, turning the pieces. Transfer to a plate.
2. Add the onion to the same pot and cook for 3 to 4 minutes. Add the tomatoes and dried Italian herbs; stir for 1 minute.
3. Return the meat and its juices. Add the pasta sauce, raisins and exactly 500 ml water. Stir, scraping the bottom of the pot, and bring to a gentle simmer.
4. Cover with the lid slightly ajar and simmer over low heat. Start checking pork after 45 minutes and beef after 90 minutes. Stir every 20 to 30 minutes so the sauce does not catch. If it becomes too thick to stir or starts sticking before the meat softens, add hot water in 50 ml portions.
5. When the meat is beginning to soften, add the potatoes and carrots. Simmer for another 30 to 40 minutes, until the vegetables are tender and a fork slides easily into the meat. Tougher beef may need longer. Keep simmering gently and add small splashes of water as needed.
6. If the stew is too thin, uncover and simmer for 5 to 10 minutes, stirring, until the sauce coats the meat. Stir in the basil leaves for the final minute, then serve.

#### Notes

- The starting water is 500 ml, not an unspecified bottle. Any extra water replaces evaporation during cooking.
- The sauce and raisin weights are suggested amounts, not conversions of the original bottle and packet.
- This is a stovetop adaptation. It replaces the unclear vacuum-pot cooking and one-hour hold with a continuous gentle simmer until the meat is tender. Add potatoes and carrots near the end so they keep their shape.

#### Source

Supplied recipe document.

<a id="minced-beef-tacos"></a>

### Minced beef for tacos

**ID:** `minced-beef-tacos`

**Servings:** 5 portions.

**Time:** About 30 minutes, including 5 to 8 minutes in the oven.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 400 g fresh minced beef
- 1 medium onion, finely diced
- 2 garlic cloves, minced
- 2 tbsp tomato paste
- 50 ml water
- 1/4 tsp ground black pepper
- 1 tsp all-purpose seasoning, or 1 tsp paprika plus 1 tsp mushroom salt
- 1 tsp dried oregano or Italian herbs
- 1 tsp garlic powder
- 1 tsp onion powder
- 1 tbsp oil
- 10 small crispy taco shells, or 10 small soft tortillas about 15 cm across
- 100 g grated cheddar or mozzarella; use 75 to 150 g for less or more cheese

#### Method

1. Heat the oven to 180°C. Set out a baking dish that holds the taco shells upright. For soft tortillas, keep them aside until the filling is ready.
2. Heat the oil in a frying pan over medium-high heat. Fry the onion for 3 to 4 minutes, until softened, then add the garlic and cook for 30 seconds.
3. Add the beef and break it into small pieces. Cook for 5 to 7 minutes. Add the pepper, chosen seasoning, dried herbs, garlic powder and onion powder, then stir for 1 minute. The beef must be cooked through and reach 71°C.
4. Stir in the tomato paste and 50 ml water. Simmer for 2 to 3 minutes, until the filling holds together and there is no puddle of liquid in the pan.
5. For crispy tacos, divide the hot filling among the 10 shells and scatter the cheese over them. Bake for 5 to 8 minutes, until the cheese melts and the shells are crisp. Check early if the shell packet gives a shorter heating time.
6. For soft tacos, warm the tortillas according to their packet instructions so they bend without cracking. Divide the filling and cheese among them, fold and arrange in the baking dish. Cover loosely with foil and bake for 5 to 8 minutes, until the cheese melts.
7. Serve immediately, with two tacos per portion.

#### Notes

- The cheese quantity and 10-shell yield are suggested additions for the existing 400 g beef filling. They make five portions of two small tacos each.
- The linked recipe supports a 180°C oven and baking the filled shells with cheese. This version retains the supplied filling quantities and seasoning choices.

#### Source

- [RecipeTin Eats: ground beef tacos](https://www.recipetineats.com/ground-beef-tacos-recipe/#recipe)

<a id="japanese-pork-stew"></a>

### Japanese pork stew

**ID:** `japanese-pork-stew`

**Servings:** 5 portions.

**Time:** Simmer the vegetables for about 30 minutes; cook the pork through and rest it for 3 minutes before serving.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 2 carrots, peeled and cut into bite-sized pieces
- 1 radish, peeled and cut into bite-sized pieces
- 1 brown onion, chopped into small pieces
- 1,000 ml water
- Dashi sachet sufficient for 1,000 ml stock, following the packet instructions
- 2 tbsp miso
- 200 g thin pork shabu slices
- 1 tsp minced ginger
- 1 tsp sesame oil

#### Method

1. Heat the sesame oil in a pot. Stir-fry the ginger and chopped onion until fragrant.
2. Add the carrots and radish and fry briefly.
3. Add the water and dashi sachet. Follow its steeping instructions and remove the sachet. Simmer the vegetables for about 30 minutes, until tender.
4. Dissolve the miso in a ladleful of the hot broth and stir it into the pot. Add the pork slices individually and separate them so they cook evenly.
5. Simmer gently until the pork is cooked through. For whole-cut pork, check for 63°C in the thickest folded slice, then leave it in the hot broth off the heat for at least 3 minutes before serving. Timing depends on slice thickness; colour alone is not a reliable check.

#### Notes

- Dashi sachets vary in strength. Use the packet's dilution instructions for the listed 1,000 ml of water.
- Chopped onion follows the ingredient list. The pork-cooking step completes the original method.

#### Source

- [Instagram recipe reference](https://www.instagram.com/reel/C7L1ZVTSoRE/)

<a id="garlicky-stir-fried-beef"></a>

### Garlicky stir-fried beef

**ID:** `garlicky-stir-fried-beef`

**Servings:** 5 portions.

**Time:** Marinate for 3 hours in the refrigerator. Suggested cooking time: about 10 minutes, plus a 3-minute beef rest.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 200 g skirt beef, cut into thin strips across the grain
- 2 sprigs spring onion, chopped, whites and greens separated
- 4 garlic cloves, minced
- 150 g bean sprouts; adjustable from 100 to 200 g
- 5 g ginger, shredded; adjustable from 3 to 8 g
- 1 tsp light soy sauce, for the marinade
- 1.5 tsp sesame oil, for the marinade
- 1 tbsp cornstarch, for the marinade
- 1/4 tsp baking soda, for the marinade
- 1 tbsp water, for the marinade
- 1 tsp light soy sauce, for the finishing sauce
- 2 tbsp water, for the finishing sauce
- 1 tbsp neutral cooking oil, divided

#### Method

1. Mix the beef with the marinade soy sauce, sesame oil, cornstarch, baking soda and 1 tbsp water. Cover and marinate in the refrigerator for 3 hours.
2. In a separate bowl, mix the finishing sauce's 1 tsp soy sauce and 2 tbsp water. Keep it separate from the raw-beef marinade.
3. Heat half the cooking oil in a large pan over medium-high heat. Add the beef in one layer, leaving excess marinade in its bowl. Fry in batches if needed until cooked through, reaching at least 63°C. Transfer to a clean plate and rest for at least 3 minutes. Discard the remaining raw marinade.
4. Reduce the heat to medium. Add the remaining oil, garlic, ginger and spring-onion whites. Fry briefly until fragrant, then add the bean sprouts and stir-fry until thoroughly cooked and steaming hot, about 3 minutes.
5. Add the prepared finishing sauce and let it bubble. Return the rested beef and its plate juices, toss until hot and coated, and add the spring-onion greens. Serve promptly.

#### Notes

- The bean-sprout amount is a suggested replacement for an undefined packet. Use 100 g for a beef-heavy dish or 200 g for more vegetables. The recorded 200 g beef is retained, so these are five small shared-dish portions.
- Ginger weight, cooking oil and the mild finishing sauce are proposed additions. The finishing sauce is separate from the recorded marinade; it is not a second batch of raw marinade.
- The source's instruction to bring raw beef to room temperature has been removed. Keep it refrigerated until the pan is ready. Cooking time depends on strip thickness, so check doneness rather than relying only on minutes per side.

#### Source

- [I Heart Umami: beef with garlic sauce](https://iheartumami.com/beef-with-garlic-sauce/)

<a id="sweet-sour-pork-ribs"></a>

### Sweet and sour pork ribs

**ID:** `sweet-sour-pork-ribs`

**Servings:** 5 portions.

**Time:** Blanch for 5 minutes; simmer for about 1 hour, then reduce the sauce until it coats the ribs.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 700 g pork ribs
- 1 sprig spring onion and 3 slices ginger, for blanching
- Enough water to cover the ribs by about 2 cm, for blanching
- 2 to 3 tbsp oil; start with 2 tbsp
- 3 tbsp rock sugar
- 500 ml hot water, for the sauce
- 2 sprigs spring onion and 5 slices ginger, for the sauce
- 1.5 tbsp Dog brand black vinegar
- 2 tbsp oyster sauce
- 2 tbsp soy sauce

#### Method

1. Put the ribs in a pot with enough water to cover by about 2 cm, 1 sprig spring onion and 3 slices ginger. Bring to a boil and blanch for 5 minutes. Drain and rinse off the foam, then pat the ribs dry.
2. Heat the oil in a pan. Add the rock sugar and stir over low heat until melted without burning it.
3. Add the ribs carefully and fry until brown and sticky.
4. Add the 500 ml hot water, remaining spring onion and ginger, vinegar, oyster sauce and soy sauce. Cover and simmer gently for about 1 hour, until tender. Add a little hot water if needed to prevent drying out.
5. Uncover and simmer, stirring and turning the ribs, until the sauce thickens and coats them. Stop before it dries out or burns. Taste and adjust the seasoning if needed.
6. Check that the thickest meat away from the bone has reached at least 63°C, then rest the ribs for 3 minutes before serving.

#### Notes

- Blanching water depends on the pot, so use the coverage instruction rather than a fixed volume.
- Sauce reduction depends on the pan and remaining liquid. A coating consistency is the endpoint; no fixed reduction time is assumed.

#### Source

- [Kitchen Misadventures: sweet and sour pork ribs](https://kitchenmisadventures.com/sweet-and-sour-pork-rib)

## Mains (rice and noodles)

<a id="fried-brown-rice-chicken"></a>

### Fried brown rice with chicken

**ID:** `fried-brown-rice-chicken`

**Servings:** 5 portions.

**Time:** Suggested: about 30 minutes with cooked, chilled rice.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 100 g corn kernels, drained if canned or thawed if frozen; adjustable from 100 to 150 g
- 100 g carrot, finely diced; adjustable from 100 to 150 g
- 200 g cabbage, shredded; adjustable from 150 to 250 g
- 6 garlic cloves, minced
- 3 eggs
- 800 g cooked, chilled brown rice; adjustable from 750 to 1,000 g
- 1 tbsp light soy sauce, for the rice
- 1 tbsp dark soy sauce
- 1/4 tsp red sugar
- 1 tbsp salt-free chicken powder
- 1 tbsp sesame oil, for frying the rice
- 1 tsp Chinese cooking wine, for the eggs
- 1/2 tsp fish sauce, for the eggs
- 150 g chicken fillet, diced
- 1 tsp cornstarch, for the chicken
- 1 tsp light soy sauce, for the chicken
- 1 tbsp neutral cooking oil, divided

#### Method

1. Beat all 3 eggs with the Chinese cooking wine and fish sauce. Mix the chicken with the cornstarch and its 1 tsp soy sauce. Mix the rice's soy sauces, sugar and chicken powder in a separate bowl.
2. Heat half the cooking oil in a large pan over medium heat. Scramble the eggs until set and transfer to a clean plate.
3. Add the remaining cooking oil and fry the chicken until cooked through, reaching 74°C. Transfer it to the plate with the cooked eggs.
4. Fry the garlic briefly in the same pan, then add the carrot, cabbage and corn. Stir-fry until the vegetables soften, then transfer them to the plate.
5. Add the sesame oil and rice to the pan. Break up clumps, stir-fry until hot, and add the rice seasoning. Return the cooked chicken, eggs and vegetables. Toss until evenly mixed and reheated to 74°C. Cook in batches if needed.

#### Notes

- Rice and vegetable amounts, chicken cornstarch and cooking oil are suggested additions. Use more cabbage or corn for a more vegetable-heavy dish.
- This version uses the ingredient list's 3 eggs throughout, resolving the source's conflicting instruction to season 2 eggs. The original 150 g chicken quantity is retained.
- Use rice that was cooled promptly and refrigerated. These are five modest portions; serve other dishes alongside if preferred.

#### Source

Supplied recipe document.

<a id="fried-basmati-rice-chicken-seafood"></a>

### Fried basmati rice with chicken and seafood

**ID:** `fried-basmati-rice-chicken-seafood`

**Servings:** 5 portions.

**Time:** Suggested: about 1 hour with cooked, chilled rice, including a 30-minute prawn soak.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 100 g ready-to-eat crab sticks, sliced; adjustable from 75 to 150 g
- 12 prawns, shelled and deveined
- 1 carrot, finely diced
- 1 cup prepared corn, using a 240 ml measuring cup
- 50 g cooked barbecue pork, shredded; adjustable from 30 to 75 g
- 2 heads garlic, peeled and minced
- 1 large shallot, sliced
- 4 eggs, beaten
- 800 g cooked, chilled basmati rice; adjustable from 750 to 1,000 g
- 1 tsp sesame oil, for the rice
- 50 g minced chicken
- 2 sprigs spring onion, chopped
- 1 tbsp fried shallots, for serving; adjustable from 1 to 2 tbsp
- 1 tsp baking soda, for the prawn soak
- 1 tsp sugar, for the prawn soak
- Enough ice water to cover the prawns
- 1 tsp light soy sauce, for the prawns
- 1/2 tsp sesame oil, for the prawns
- 1/2 tsp cornstarch, for the prawns
- 1 tsp chicken bouillon mixed with 1 tsp water
- 1/8 tsp ground black pepper, plus more to taste
- 2 tbsp neutral cooking oil, divided

#### Method

1. Soak the prawns in the baking soda, sugar and ice water for 30 minutes in the refrigerator. Drain, rinse and pat dry. Mix with the light soy sauce, 1/2 tsp sesame oil and cornstarch. Toss the chilled rice with its 1 tsp sesame oil.
2. Reserve 1 tsp minced garlic for the prawns. Split the remaining garlic and the shallot into two equal portions.
3. Heat 1/2 tbsp cooking oil in a large pan over medium heat. Scramble the eggs until set and transfer to a clean plate.
4. Add 1/2 tbsp oil and the reserved 1 tsp garlic. Add the prawns and stir-fry until firm and opaque throughout. Add the crab sticks, heat through, then transfer both to the plate with the cooked eggs.
5. Add 1/2 tbsp oil and one portion of garlic and shallot. Fry briefly, add the carrot and corn, and stir-fry until the carrot softens. Transfer the vegetables to the plate.
6. Add the remaining 1/2 tbsp oil, garlic and shallot. Fry briefly, then add the minced chicken. Break it up and cook until it reaches 74°C. Add the cooked barbecue pork and rice, then the bouillon mixture. Stir-fry until the rice is hot throughout.
7. Return the cooked eggs, vegetables and seafood. Add the pepper and spring onion, toss until everything is reheated to 74°C, and serve with fried shallots. Use two batches if the pan is crowded.

#### Notes

- The rice amount is a new working quantity for five portions. The source's 1 cup did not say whether the rice was cooked or dry, so it has not been treated as an equivalent weight.
- Crab-stick and barbecue-pork weights, cornstarch, oil, pepper and garnish amounts are suggested additions. The source's 2 heads of garlic are retained; this is a garlic-heavy version.
- Use rice that was cooled promptly and refrigerated. Keep prawns refrigerated during the soak.

#### Source

Supplied recipe document.

<a id="fried-brown-rice-reduced-seasoning"></a>

### Fried brown rice, reduced seasoning

**ID:** `fried-brown-rice-reduced-seasoning`

**Servings:** 5 portions.

**Time:** Suggested: about 30 minutes with cooked, chilled rice.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 1 sprig spring onion, chopped, whites and greens separated
- 50 g prepared corn
- 1/2 carrot, finely diced
- 50 g cabbage, shredded
- 8 garlic cloves, minced
- 10 g ginger, minced; adjustable from 5 to 15 g
- 3 eggs
- 800 g cooked, chilled brown rice; adjustable from 750 to 1,000 g
- 1 tbsp light soy sauce, for the rice
- 1 tbsp dark soy sauce
- 1/4 tsp red sugar
- 1 tbsp salt-free chicken powder
- 1/2 tsp Chinese cooking wine, for the eggs
- 1/4 tsp fish sauce, for the eggs
- 150 g chicken fillet, diced
- 1 tsp cornstarch, for the chicken
- 1 pinch mushroom salt, for the chicken
- 3 tbsp neutral cooking oil, divided

#### Method

1. Beat the eggs with the Chinese cooking wine and fish sauce. Mix the chicken with the cornstarch and mushroom salt. Mix the rice's soy sauces, sugar and chicken powder in a separate bowl.
2. Heat 1 tbsp oil over medium heat. Scramble the eggs until set and transfer to a clean plate.
3. Add 1 tbsp oil, the garlic and ginger. Fry until fragrant but not dark brown. Add the chicken and spring-onion whites. Stir-fry until the chicken is cooked through, reaching 74°C, then transfer to the plate with the cooked eggs.
4. Add the carrot, corn and cabbage to the same pan. Stir-fry until softened, then transfer to the plate.
5. Add the remaining 1 tbsp oil and the rice. Break up clumps and stir-fry until hot. Add the rice seasoning, return the cooked chicken, eggs and vegetables, and toss until reheated to 74°C. Finish with the spring-onion greens.

#### Notes

- The rice amount is a new working quantity for five portions. The source's 1 cup did not specify cooked or dry rice; it has not been converted into this weight.
- Ginger weight and chicken cornstarch are suggested additions. Other recorded quantities are retained.
- The source calls this a reduced-seasoning version for serving with other dishes; it is not a low-sodium claim. Its alternative pork title has no separate pork method, so this version uses chicken.
- Use rice that was cooled promptly and refrigerated.

#### Source

Supplied recipe document.

<a id="miso-butter-corn-fried-rice-chicken"></a>

### Miso butter corn fried rice with chicken

**ID:** `miso-butter-corn-fried-rice-chicken`

**Servings:** 5 portions.

**Time:** Suggested: about 25 minutes with cooked, chilled rice.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 3/4 tbsp miso paste mixed with 1 tbsp water
- 150 g canned corn, drained; adjustable from 100 to 200 g; reserve 2 tbsp of its liquid
- 1 cup cooked, chilled rice, using a 240 ml measuring cup; brown rice is suitable
- 1/2 zucchini, diced
- 1 carrot, finely diced
- 150 g chicken, sliced
- 1 tsp cornstarch, for the chicken
- 1/2 tsp light soy sauce, for the chicken
- 3 garlic cloves, minced
- 1 tbsp olive oil, divided
- 1 tbsp butter
- 2 tbsp reserved corn liquid

#### Method

1. Mix the chicken with the cornstarch and soy sauce. Break up any clumps in the chilled rice.
2. Heat half the olive oil over medium heat. Fry the garlic briefly, add the zucchini and carrot, and stir-fry until softened. Transfer to a clean plate.
3. Add the remaining olive oil. Fry the chicken until cooked through, reaching 74°C, then transfer it to the plate with the vegetables.
4. Melt the butter in the pan, add the drained corn and 2 tbsp reserved corn liquid, and cook until most of the liquid evaporates.
5. Add the rice and the miso mixture. Stir-fry until the rice is hot and no liquid pools in the pan. Return the cooked chicken and vegetables and toss until reheated to 74°C.

#### Notes

- The source's 1 cup of cooked rice is retained. A 240 ml measuring cup is the suggested working measure. This makes five small side portions, not five full rice meals.
- Corn, cornstarch and olive-oil quantities are suggested additions. The method now uses the listed miso mixture.
- Use rice that was cooled promptly and refrigerated, including overnight rice. Never leave cooked rice at room temperature overnight.

#### Source

Supplied recipe document.

<a id="soya-mee-soup"></a>

### Soya mee soup

**ID:** `soya-mee-soup`

**Servings:** 5 portions.

**Time:** Suggested: 20 minutes preparation and about 70 minutes cooking. Prepare the toppings during the stock simmer; black-fungus soaking can overlap.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 150 g minced pork or chicken; choose one
- 1 tbsp minced garlic
- 10 g dried black fungus, weighed before soaking
- 40 g dried anchovies, rinsed twice; use 30 to 50 g
- 10 whole prawns, peeled and deveined, shells reserved for stock, or 300 g raw chicken bones; use 250 to 400 g bones
- 150 g cooked, drained yellow soybeans; use 100 to 200 g
- 1 sweet date
- 300 g dry soya mee; use 250 to 350 g
- 4 hard-boiled eggs, peeled and cut into wedges
- 300 g leafy vegetables such as bok choy, stems and leaves separated; use 250 to 400 g
- 2 slices ginger
- 1/2 tbsp light soy sauce, for the mince
- 1 tbsp sesame oil, for the mince
- 1 tsp cornstarch, for the mince
- 1 tbsp oyster sauce
- 100 ml water, for the mince mixture
- 1 tbsp neutral cooking oil, for the mince mixture
- 1.5 litres water for the stock, plus extra hot water to restore the strained stock to 1.5 litres
- Water for soaking the fungus and cooking the noodles

**Optional toppings**

- 6 small shallots, peeled and thinly sliced
- 2 tbsp neutral cooking oil, only if frying the shallots
- 15 g ready-fried anchovies; use 10 to 20 g

#### Method

1. If using prawns, keep the peeled meat covered in the fridge while making stock. Put their reserved shells, or the chicken bones, in a pot with the ginger, sweet date, rinsed dried anchovies, cooked soybeans and 1.5 litres water. Bring to a full boil, then cover partly and simmer for about 1 hour. Add hot water during simmering if needed to keep the ingredients submerged.
2. Meanwhile, rinse the dried fungus and cover with plenty of clean water. Soak for about 20 to 30 minutes, or according to its label, until expanded and flexible. Follow the collection's soaking guidance. Drain, rinse, trim off hard bases and shred. Discard its soaking water.
3. For the optional shallot topping, heat its 2 tbsp oil in a small pan over medium-low heat. Fry the sliced shallots for about 5 to 8 minutes, stirring, until pale golden. Remove with a slotted spoon and drain; they darken as they cool.
4. Mix the mince with the light soy sauce, sesame oil and cornstarch. Heat its 1 tbsp neutral oil in a separate pan and fry the garlic for about 30 seconds. Add the mince, break up clumps and cook through to 71°C for pork or 74°C for chicken. Add the drained fungus, oyster sauce and the separate 100 ml water. Simmer for about 5 minutes, until the fungus is cooked and the mixture is hot throughout. Keep hot.
5. Strain the stock into a clean pot and discard the bones or shells, ginger, date and stock solids. Measure the strained liquid and add hot water to make 1.5 litres. Bring back to a simmer.
6. Add the vegetable stems and simmer for about 2 minutes. If using prawns, add their reserved meat now. Add the vegetable leaves and simmer for about 2 to 4 minutes, until the greens are tender and the prawns are firm and opaque throughout. Add the hard-boiled egg wedges for the final minute to warm them.
7. Cook the soya mee separately according to its label and drain. Divide among five bowls. Add the mince-and-fungus mixture, greens, egg and prawns if used. Ladle over the stock and finish with the optional fried shallots and ready-fried anchovies.

#### Notes

- Noodle, leafy-vegetable and anchovy weights, chicken-bone weight, stock volume and topping amounts are suggested working quantities. They replace undefined bundles, a bunch, cups and missing measures, rather than recover the original amounts. This adaptation has not been kitchen-tested.
- Use 250 g dry noodles for a lighter bowl or 350 g for more noodles. Cook them separately so they do not absorb the measured soup stock before serving.
- The source does not state whether its yellow beans are dry or cooked. This adaptation explicitly uses cooked yellow soybeans as a stock ingredient. Do not put the same weight of raw dry soybeans straight into this method. The stock solids are strained out before serving.
- Choose the prawn stock or chicken-bone stock. The prawn version reserves the peeled meat for a brief cook near serving time; it does not simmer the meat for an hour.
- The source's 10 g black fungus is treated as a proposed dry weight. The 1.5 litres of finished stock and the separate 100 ml mince liquid are both counted in the recipe; soaking and noodle water are discarded.
- Four eggs are retained. Cut them into wedges to share across five portions.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.instagram.com/reel/C4sYVukySZ1/)

<a id="vietnamese-beef-noodle-soup"></a>

### Vietnamese beef noodle soup

**ID:** `vietnamese-beef-noodle-soup`

**Servings:** 5 portions.

**Time:** Suggested stovetop estimate: 20 minutes preparation and 2.5 to 3.5 hours gentle simmering; use tenderness to judge the finish.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 500 g oxtail, cut into sections
- 400 g beef brisket, cut into large chunks
- 1 radish, peeled and cut into chunks
- 1 carrot, cut into chunks
- 1 onion, quartered
- 2 spring onions, cut into lengths
- 4 slices ginger
- 3 star anise
- 5 cloves
- 3 bay leaves
- 1.5 litres water, plus hot water to keep the meat just covered during cooking
- 1 tbsp oyster sauce
- 2 tbsp soy sauce
- 300 g spinach, trimmed; adjust from 250 to 400 g
- 300 g dry mung-bean noodles; adjust from 250 to 350 g
- 15 g coriander, roughly chopped; adjust from 10 to 20 g

#### Method

1. Put the oxtail and brisket in a pot that holds them snugly. Add 1.5 litres water and a little more if needed to just cover the meat. Bring to a boil and skim off the foam.
2. Add the onion, spring onions and ginger. Put the star anise, cloves and bay leaves in a spice bag or infuser and add it to the pot. Reduce to a gentle simmer and cover partly.
3. Simmer for about 2.5 to 3.5 hours, until the brisket is fork-tender and the oxtail meat releases easily from its bones. Check periodically and add hot water to keep the meat just covered. Remove the brisket earlier if it becomes tender before the oxtail.
4. About 45 minutes before the meat is expected to be tender, add the radish and carrot. Add the oyster sauce and soy sauce for the final 15 minutes. Continue until the vegetables are tender. Return any reserved brisket and heat through, then remove the spice bag and coarse aromatics.
5. Prepare the mung-bean noodles in a separate pot according to their packet, then drain. Blanch the spinach until wilted and drain.
6. Remove any loose bones from the broth. Divide the noodles, spinach, meat and root vegetables among five bowls. Ladle over the hot broth and finish with coriander.

#### Notes

- This is a proposed stovetop adaptation. The source says only to use a vacuum pot for two hours; that incomplete instruction is not carried over as a thermal-cooker procedure.
- The noodle, spinach and coriander amounts are suggested defaults. Use fewer noodles for a broth-heavy bowl, or more noodles for larger appetites. Coriander can stay at the lower end for a milder garnish.
- The original 1.5 litres water is the starting amount. Pot shape and evaporation determine how much extra water is needed during the long simmer. Cook noodles separately so they do not consume the soup broth.
- Oxtail and brisket need time to become tender. The suggested time is an estimate, not a tested guarantee.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.instagram.com/reel/DZpmSdLBlOw/)

<a id="coconut-chicken-noodle-soup"></a>

### Coconut chicken noodle soup

**ID:** `coconut-chicken-noodle-soup`

**Servings:** 5 portions.

**Time:** Vacuum pot: 2 hours; wolfberries added for the final 15 minutes.

**Review:** Imported draft.

#### Ingredients

- Water from 2 coconuts
- Flesh from 1 coconut
- 1 chicken
- 800 ml water
- 2 corn cobs
- 2 tbsp dried scallops
- 5 red dates
- 1 tbsp wolfberries
- Spinach, for serving, quantity not specified
- Noodles, for serving, quantity not specified

#### Method

1. Boil in a vacuum pot for 2 hours. Add the wolfberries for the final 15 minutes.
2. Serve with spinach and noodles.

#### Notes

- The source gives coconut water by coconut count, not volume. Noodle and spinach cooking instructions are not specified.

#### Source

Supplied recipe document.

<a id="oyakodon"></a>

### Oyakodon

**ID:** `oyakodon`

**Servings:** 5 portions.

**Time:** Suggested estimate: 10 minutes preparation and 15 minutes cooking, plus rice cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 2 tbsp sukiyaki sauce
- 1.5 tbsp mirin
- 1 tbsp sake
- 160 ml water
- 1/2 tsp brown sugar, optional
- 2 boneless chicken thighs, cut into bite-sized pieces
- 1 large yellow onion, thinly sliced
- 2 spring onions, thinly sliced; adjust from 1 to 3
- 2 eggs
- 900 g cooked rice, hot for serving; adjust from 750 to 1,000 g

#### Method

1. Combine the sukiyaki sauce, mirin, sake, water and optional sugar in a wide pan. Add the yellow onion, bring to a simmer and cook for about 5 minutes, until the onion starts to soften.
2. Add the chicken in one layer. Cover and simmer gently for about 6 to 10 minutes, turning the pieces as needed, until the thickest piece reaches 74°C. Keep the chicken and sauce in the pan.
3. Lightly beat the eggs, leaving some streaks of white and yolk. Pour two-thirds over the simmering chicken. Cover for about 1 minute until partly set.
4. Add the remaining egg and spring onion. Cover and cook gently until the egg is set and the chicken-and-egg mixture reaches 74°C. Use doneness rather than the estimated time to decide when it is ready.
5. Divide the hot rice among five bowls and spoon the chicken, egg and sauce over it.

#### Notes

- The suggested rice and spring-onion amounts fill the source gaps. Use less rice for a lighter meal and more for larger appetites.
- The original quantities of two chicken thighs and two eggs are unchanged. These make a modest topping across five portions.
- This proposed method adds the missing sauce and spring-onion steps. It cooks the egg through rather than leaving a runny topping.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.justonecookbook.com/oyakodon/)

<a id="ginger-scallion-chicken-rice-noodles"></a>

### Ginger scallion chicken rice noodles

**ID:** `ginger-scallion-chicken-rice-noodles`

**Servings:** 5 portions.

**Time:** Suggested estimate: 15 minutes preparation and 20 minutes cooking, plus black-fungus soaking according to its packet.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 900 g fresh thick rice noodles, also called laksa noodles; adjust from 800 to 1,000 g
- 300 g leafy vegetables, such as nai bai, cut up; adjust from 250 to 400 g
- 8 slices ginger
- 2 spring onions, whites and greens separated and cut into lengths
- 4 large fresh mushrooms, sliced
- 10 g dried black fungus, soaked according to its packet, rinsed, trimmed and torn into bite-sized pieces
- 600 g boneless chicken, cut into bite-sized pieces
- 1 tbsp cornstarch
- 1.5 tbsp soy sauce
- 2 tbsp dark soy sauce
- 2 tbsp Chinese cooking wine
- 1 tbsp sesame oil
- 200 ml water, plus 50 ml additions if needed
- 1 tbsp neutral cooking oil

#### Method

1. Prepare the black fungus according to its packet. Coat the chicken with the cornstarch, soy sauce, dark soy sauce, cooking wine and sesame oil. Separate the leafy-vegetable stems from the leaves.
2. Loosen or blanch the fresh rice noodles according to their packet, then drain. Do not use the same weight of dry noodles as a direct substitute.
3. Heat the neutral oil in a large wok or pan. Fry the ginger and white parts of the spring onions until fragrant. Add the mushrooms and prepared black fungus and stir-fry for 1 minute.
4. Add the chicken and its marinade. Stir-fry for about 3 minutes, then add 200 ml water. Bring to a simmer, cover and cook for about 5 to 8 minutes, until the thickest chicken piece reaches 74°C. Stir occasionally so the sauce does not catch.
5. Add the vegetable stems and simmer for 2 minutes. Fold in the noodles, vegetable leaves and green parts of the spring onions. Toss gently for another 2 to 3 minutes, until the leaves are tender and the noodles are hot throughout. If the pan dries before everything cooks, add water in 50 ml amounts.
6. Divide among five portions and serve hot.

#### Notes

- The suggested fresh-noodle weight replaces the unrecognised source unit "1 pts". Use more noodles for a fuller meal or more greens for a vegetable-heavy balance.
- This adaptation defines the source's 10 g black fungus as its dry weight and the four mushrooms as fresh mushrooms. These are proposed forms, not recovered source details.
- The existing 600 g chicken and marinade quantities are unchanged. The 200 ml water makes a coating sauce rather than a noodle soup.

#### Source

Supplied recipe document.

<a id="soy-milk-ramen"></a>

### Soy milk ramen

**ID:** `soy-milk-ramen`

**Servings:** 5 portions.

**Time:** Suggested estimate: 25 minutes active preparation, 30 to 60 minutes soaking and 1 hour broth simmering. Cook toppings during the broth simmer.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 1 kombu sheet, about 10 cm long
- 12 small dried mushrooms
- 1.5 litres water, plus hot water to replace evaporation
- 2 tbsp minced garlic, for the soup base
- 3 tsp minced ginger, for the soup base
- 1 onion, chopped
- 2 tbsp sesame oil, for the soup base
- 1 corn cob, cut into pieces, for the soup base
- 1 carrot, cut into chunks
- 1 sweet date
- 2.5 tbsp miso
- 300 ml unsweetened soy milk
- 350 g dry ramen noodles; adjust from 300 to 400 g
- 200 g corn kernels, fresh or frozen, for serving; adjust from 150 to 250 g
- 300 g nai bai, trimmed and cut up; adjust from 250 to 400 g
- 100 g shimeji mushrooms, roots trimmed; adjust from 75 to 150 g
- 300 g silken tofu, drained and cubed; adjust from 250 to 350 g
- 400 g boneless chicken, thinly sliced; adjust from 300 to 500 g
- 1 tsp soy sauce, 1/2 tsp sesame oil and 1 tsp cornstarch, for marinating the chicken
- 1 garlic clove, minced, and 1 tsp minced ginger, for frying the chicken
- 1 tsp neutral cooking oil, for frying the chicken
- 5 eggs

#### Method

1. Wipe visible grit from the kombu without scrubbing away its white coating. Rinse the dried mushrooms. Soak the kombu and mushrooms in 1.5 litres water for 30 to 60 minutes. Coat the chicken with soy sauce, sesame oil and cornstarch and refrigerate while making the broth.
2. Fry the soup-base garlic, ginger and onion in 2 tbsp sesame oil until fragrant. Add the soaked ingredients and their water, the corn cob, carrot and sweet date. Heat gently and remove the kombu just before boiling. Simmer for 1 hour, partly covered. Add hot water as needed to maintain the original liquid level.
3. Remove the corn cob, carrot, date and dried mushrooms from the broth. Slice the cooked mushrooms for serving; the cooked carrot and corn can also be served as toppings. Discard the date pit if present.
4. Boil the eggs until the whites and yolks are firm, about 10 to 12 minutes for large eggs. Cool enough to handle, peel and halve.
5. Heat 1 tsp neutral oil in a frying pan. Fry the topping garlic and ginger briefly, add the chicken and stir-fry until the thickest piece reaches 74°C, about 5 to 8 minutes depending on thickness.
6. Cook the ramen in a separate pot according to the packet and drain. Add the serving corn, shimeji, nai bai and tofu to the broth. Simmer for about 3 to 5 minutes, until the vegetables and mushrooms are cooked and the tofu is hot throughout.
7. Mix the miso with a little hot broth until smooth, then stir it back into the pot. Add the soy milk and heat gently until hot; avoid a rolling boil.
8. Divide the noodles among five bowls. Ladle over the soup and vegetables, then add the chicken, eggs and reserved mushroom slices. Serve immediately.

#### Notes

- Suggested weights replace the unknown noodle packets, topping packets and chicken amount. Choose more chicken or tofu for a heartier bowl, or more greens for a lighter balance. Cook noodles separately to preserve the soup volume.
- This adaptation interprets the chicken marinade's unspecified "sesame" as sesame oil and supplies the missing cornstarch and frying-aromatic amounts.
- The unidentified soup pack is omitted. The existing miso provides the soup seasoning; taste the finished broth before making any further seasoning adjustment.
- The original 1.5 litres water and 300 ml soy milk are retained. Replace water lost during the long simmer before adding the soy milk.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.instagram.com/reel/C9ujt4ISo-T/)

<a id="stir-fried-beehoon-fish-chicken"></a>

### Stir-fried beehoon with fish or chicken

**ID:** `stir-fried-beehoon-fish-chicken`

**Servings:** 5 portions.

**Time:** About 45 to 60 minutes, plus any longer soak required by the optional dried beancurd sticks. Final noodle cooking takes about 5 to 8 minutes.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 300 g dry brown-rice beehoon; use 250 to 350 g for smaller or larger noodle portions
- Water for soaking the beehoon, enough to cover by 2 cm; drain before cooking
- 5 garlic cloves, minced
- 1 large shallot, thinly sliced
- 1 tbsp dried shrimp
- 150 ml warm water, for soaking the shrimp; discard after soaking
- 250 g cabbage, finely shredded; use 200 to 350 g
- 120 g carrot, coarsely grated; use 100 to 150 g
- 30 g dried beancurd sticks, optional; use 20 to 50 g
- Water for soaking the beancurd sticks, enough to cover by 2 cm; drain before cooking
- 200 g bean sprouts, rinsed and drained; use 150 to 250 g
- 4 eggs
- 1/2 tsp fish sauce and 1/2 tsp sesame oil, for the eggs
- 200 g boneless white fish, such as snapper or tilapia, thinly sliced; or 2 boneless chicken thighs, cut into 2 cm cubes
- 1 tsp cornflour and 1 tsp soy sauce, for the fish or chicken marinade
- 1 tbsp oyster sauce
- 1 tbsp soy sauce, for the noodles
- 1 tbsp black soy sauce
- 1/2 tsp sugar
- 250 ml water, for the noodle seasoning, plus up to 250 ml hot water if the noodles need it
- 1/2 tsp chicken bouillon powder
- 3 tbsp cooking oil, divided
- 150 g optional extras in total; use 100 to 200 g of trimmed snow peas, sweetcorn, thinly sliced mushrooms or sliced cooked fish cake

#### Method

1. If using dried beancurd sticks, soak in enough warm water to cover by 2 cm for 30 to 60 minutes, or the packet time, until soft throughout. Thick sticks can take longer. Drain and cut into short pieces. Soak the dried shrimp in 150 ml warm water for 15 to 20 minutes, then drain and roughly chop.
2. Soak the beehoon in room-temperature water for 20 to 30 minutes, or the packet's stir-fry preparation time, until bendable but still firm. Drain well. Meanwhile, mix the fish or chicken with its cornflour and 1 tsp soy sauce; refrigerate for 10 minutes. Beat the eggs with the fish sauce and sesame oil.
3. Mix the oyster sauce, remaining 1 tbsp soy sauce, black soy sauce, sugar, bouillon and 250 ml water in a jug. Keep the extra hot water separate.
4. Heat 1 tbsp cooking oil in a large wok over medium-high heat. Fry the fish for about 2 to 4 minutes, until it reaches 63°C, or the chicken for 5 to 7 minutes, until it reaches 74°C. Transfer to a clean plate. Add a second tbsp oil and scramble the eggs until fully set; transfer to the same plate.
5. Add the remaining tbsp oil. Fry the garlic, shallot and drained shrimp for 1 minute. Add the beancurd sticks, cabbage, carrot and any optional extras. Stir-fry for 3 to 4 minutes, until the cabbage starts to soften.
6. Add the drained beehoon and the seasoning mixture. Toss over medium heat for about 5 to 8 minutes, until the noodles are tender and have absorbed most of the liquid. If the pan dries out while the noodles are still firm, add hot water 50 ml at a time and keep tossing. Do not add all the extra water automatically.
7. Add the bean sprouts, cooked eggs and fish or chicken for the final 2 minutes. Toss until the sprouts are cooked and steaming hot and the eggs are fully set, then serve.

#### Notes

- The noodle, vegetable and beancurd weights are suggested amounts. They replace unspecified packets and stick sizes without claiming to recover the original pack weights.
- Choose the lower noodle amount with more vegetables or other dishes. At the higher end, expect to use more of the reserved hot water.
- The 3 tbsp oil covers all frying stages; do not add a fresh 3 tbsp at the vegetable stage.
- Brown-rice noodle brands soften at different speeds. Follow the packet's stir-fry soak instructions when they differ, then use tenderness to judge the final cooking time.

#### Source

Supplied recipe document.

<a id="tomato-curry-udon"></a>

### Tomato curry udon

**ID:** `tomato-curry-udon`

**Servings:** 5 portions.

**Time:** Suggested estimate: 15 minutes preparation and 25 minutes cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 4 tomatoes, peeled and diced
- 2 onions, diced
- 60 g Japanese curry roux; adjust from 40 to 70 g according to the brand and desired thickness
- 1/2 tsp curry powder, optional; use up to 1 tsp for more curry flavour
- 1 apple, cored and grated, or 30 g raisins; adjust raisins from 20 to 40 g
- 1.2 litres prepared dashi stock
- 300 g minced pork or chicken; adjust from 250 to 400 g
- 1 tsp cornstarch and 1 tsp soy sauce, for marinating the meat
- 300 g firm or silken tofu, drained and cubed; adjust from 250 to 400 g
- 1,000 g fresh or frozen cooked udon; adjust from 800 to 1,000 g
- 400 g leafy vegetables, cut up; adjust from 300 to 500 g
- 1 tbsp neutral cooking oil

#### Method

1. Mix the minced meat with the cornstarch and soy sauce. Heat the oil in a pot. Fry the meat and diced onions, breaking up the mince, until the onions start to soften.
2. Add the tomatoes and cook until softened and pulpy. Stir in the dashi and grated apple or raisins. Bring to a simmer and cook for about 15 minutes, until the onions and tomatoes are soft. Confirm chicken mince reaches 74°C or pork mince reaches 71°C.
3. Lower the heat. Dissolve 40 g of the curry roux in a ladleful of hot broth and stir it into the pot. Simmer gently, stirring, until dissolved and slightly thickened. Add more roux in 10 g amounts if needed, up to 70 g. The default total is 60 g; taste for salt before adding more.
4. For more curry flavour without more roux, mix the optional curry powder into a little broth, stir it in and simmer for at least 3 minutes. Add the tofu and vegetable stems, followed by the leaves. Simmer until the greens are tender and the tofu is hot throughout.
5. Prepare the udon separately according to its packet. Drain and divide among five bowls. Spoon over the curry, meat, tofu and vegetables.

#### Notes

- The suggested roux weight replaces three cubes of unknown size. Brands differ in salt and thickening strength, so use the lower amount first. This is a soupy curry for udon.
- Use the lower udon and meat amounts for smaller appetites, or more tofu and greens for a vegetable-heavy bowl. Bob should choose one amount within each range before producing a shopping list.
- The existing 1.2 litres dashi is retained. The proposed method now cooks the noodles, tofu and greens and states when to add the extra curry powder.
- Tracking parameters and an embedded access token were removed from the original recipe link.

#### Source

Supplied recipe document.

- [Original recipe link](https://daigasikfaan.co/15-minute-tomato-beef-curry-udon/)

<a id="seafood-white-beehoon"></a>

### Seafood white beehoon

**ID:** `seafood-white-beehoon`

**Servings:** 5 portions.

**Time:** Suggested estimate: 30 minutes preparation and 45 minutes cooking. Prawn soak: 30 minutes in the fridge, which can overlap with preparation.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 6 garlic cloves, minced and divided
- 1 spring onion, cut into lengths
- 2 large slices ginger
- 15 prawns, peeled and deveined; reserve the shells and legs for stock
- 600 g live shell-on clams, scrubbed; adjust from 400 to 800 g
- 250 g boneless fish, sliced; adjust from 200 to 300 g
- 1 tsp cornstarch and 1 tsp sesame oil, for marinating the fish
- 4 eggs, beaten
- 100 g pork collar, thinly sliced
- 300 g leafy vegetables, cut into bite-sized pieces; adjust from 250 to 400 g
- 1/2 cup cooked yellow soybeans, for the stock
- 350 g dry beehoon; adjust from 300 to 400 g
- 2 litres low-sodium chicken stock in total; start with 1.5 litres and reserve 500 ml
- 1/2 tsp ground white pepper
- 1/2 tbsp fish sauce; use up to 1 tbsp after tasting
- 1 tbsp cooking wine; use up to 1.5 tbsp
- 1 tsp baking soda and 1 tsp sugar, for soaking the prawns
- Cold water, enough to cover the prawns
- 1 tsp sesame oil and 1 tsp soy sauce, for marinating the prawns
- 1 tsp cornstarch, for marinating the prawns; use up to 2 tsp for a slightly thicker coating
- 2 tbsp neutral cooking oil, divided

#### Method

1. Discard cracked clams and any open ones that do not close when tapped. Keep the clams refrigerated while preparing the stock. Soak the prawns in cold water with the baking soda and sugar for 30 minutes in the fridge. Rinse and drain, then coat with their sesame oil, soy sauce and cornstarch. Coat the fish with its cornstarch and sesame oil and keep both refrigerated.
2. Heat 1 tsp of the cooking oil in a pot. Fry the prawn shells and legs with the ginger and spring onion until fragrant. Add the cooked yellow soybeans and 1.5 litres of the stock. Simmer for 30 minutes, then strain and discard the stock solids. Keep the remaining 500 ml stock ready to add later.
3. Prepare the beehoon according to its packet until pliable but not fully cooked, then drain. Separate the vegetable stems from the leaves.
4. In a large wok or pot, heat 2 tsp oil. Scramble the eggs until fully set, then transfer them to a clean bowl. Heat the remaining 1 tbsp oil and fry all the minced garlic briefly. Add the pork collar and stir-fry for about 2 minutes.
5. Pour in the strained stock, white pepper, 1/2 tbsp fish sauce and 1 tbsp cooking wine. Bring to a boil. Add the beehoon, vegetable stems and clams, cover and simmer for about 3 minutes.
6. Add the prawns, fish and vegetable leaves. Simmer for another 3 to 5 minutes, gently turning the noodles, until the noodles are tender, the prawns are firm and opaque, the fish reaches 63°C and the pork reaches 71°C. Continue cooking any seafood that has not reached its endpoint. Discard clams that remain closed.
7. Stir in the cooked eggs. Add reserved stock in 100 ml amounts if the noodles need more liquid. Return to a simmer and taste before adding the remaining fish sauce or cooking wine. Divide among five portions and serve hot.

#### Notes

- This adaptation uses 2 litres of prepared stock in total. It resolves the ambiguous original packet instruction; it does not claim the original meant exactly 2 litres.
- The clam and noodle weights replace unmeasured scoops and bundles. More noodles make a drier, more filling dish; use more of the reserved stock with the upper noodle amount.
- The default fish quantity is 250 g within the source's 200 to 300 g range. More clams and greens can be chosen without changing the base seasoning automatically.
- The source does not identify the form of the yellow beans. This adaptation specifies cooked yellow soybeans for the stock, then strains them out with the prawn shells.
- The proposed finishing steps cook the seafood fully rather than stopping at the source's partly cooked stage.

#### Source

Supplied recipe document.

- [Original recipe link](https://whattocooktoday.com/singapore-seafood-white-bee-hoon.html)

<a id="white-braised-hokkien-mee"></a>

### White braised Hokkien mee

**ID:** `white-braised-hokkien-mee`

**Servings:** 5 portions.

**Time:** Suggested estimate: 25 minutes preparation and 45 minutes cooking. Prawn soak: 30 minutes in the fridge, which can overlap with preparation.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 6 garlic cloves, minced
- 1 spring onion, cut into lengths
- 2 large slices ginger
- 1/2 onion, thinly sliced
- 8 prawns, peeled and deveined; reserve the shells and legs for stock
- 300 g live shell-on clams, scrubbed; adjust from 250 to 500 g
- 200 g boneless fish, sliced, optional
- 1 tsp cornstarch and 1 tsp sesame oil, for marinating the optional fish
- 2 eggs
- 1 tbsp cornstarch and 3 tbsp cold water, for the egg slurry
- 100 g pork collar, thinly sliced
- 1 tsp cornstarch, 1 tsp sesame oil, 1/8 tsp salt and 1/8 tsp white pepper, for marinating the pork collar
- 50 g pork belly, thinly sliced, optional
- 175 g bok choy and 175 g Chinese spinach, cut up; adjust from 300 to 450 g combined
- 800 g fresh yellow noodles; adjust from 750 to 1,000 g
- 150 g seafood tofu, sliced; adjust from 100 to 200 g
- 1 litre chicken broth
- 1 tbsp cooking wine
- 1/2 tsp ground white pepper, for the broth
- 1 tsp baking soda and 1 tsp sugar, for soaking the prawns
- Cold water, enough to cover the prawns
- 1 tsp cornstarch and 1/2 tsp soy sauce, for marinating the prawns
- 1 tbsp neutral cooking oil
- Salt, to taste; start with none
- Hot water, in 100 ml additions if needed

#### Method

1. Discard cracked clams and any open ones that do not close when tapped. Keep the clams refrigerated. Soak the prawns in cold water with the baking soda and sugar for 30 minutes in the fridge, then rinse and drain. Coat the prawns, pork collar and optional fish with their separate marinades and keep refrigerated.
2. Heat 1 tsp oil in a pot. Fry the prawn shells and legs with the ginger and spring onion until fragrant. Add the chicken broth and simmer for 30 minutes. Strain and discard the shells and aromatics.
3. Loosen or blanch the fresh noodles according to the packet and drain. Blanch the Chinese spinach separately until just tender, then drain. Reserve the bok choy, with stems and leaves separated.
4. Mix 1 tbsp cornstarch with 3 tbsp cold water until smooth, then beat it into the two eggs. Stir again just before pouring it into the broth.
5. Heat the remaining 2 tsp oil in a large wok or pot. If using pork belly, fry it first until some fat renders. Add the sliced onion and garlic and fry until the onion softens. Add the marinated pork collar and stir-fry for about 2 minutes.
6. Add the strained broth, cooking wine, ground white pepper, seafood tofu, vegetable stems and clams. Bring to a simmer, cover and cook for about 3 minutes. Add the prawns, optional fish, noodles and vegetable leaves. Simmer for another 3 to 5 minutes, until the noodles are tender, the pork reaches 71°C, the prawns are firm and opaque, and any fish reaches 63°C. Discard clams that remain closed.
7. Lower the heat to a gentle simmer. Stir the egg slurry again, pour it in slowly and stir gently to form soft egg ribbons. Simmer until the egg is set and reaches 71°C and the broth thickens, about 1 to 2 minutes. Fold in the drained spinach and heat through.
8. Taste before adding salt, a small pinch at a time. Add hot water in 100 ml amounts if the noodles absorb too much broth. Divide among five portions and serve hot.

#### Notes

- The noodle, clam, seafood-tofu and combined vegetable weights are suggested replacements for packets, scoops and bunches. Use more noodles for a fuller meal, or more greens for a vegetable-heavy version.
- The existing 1 litre of broth and egg-slurry quantities are retained. The method now explains the slurry, onion, greens and final seafood cooking.
- Salt is optional after tasting the broth and noodles. The source's unspecified stock-paste alternative is omitted from this adaptation to avoid adding an unknown second dose of concentrated stock.

#### Source

Supplied recipe document.

<a id="dashi-garlic-butter-fried-rice"></a>

### Dashi garlic butter fried rice

**ID:** `dashi-garlic-butter-fried-rice`

**Servings:** 5 portions.

**Time:** Suggested: about 50 minutes, including cooking the rice.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 1 tbsp olive oil, divided
- 2 tbsp unsalted butter
- 10 garlic cloves, pressed
- 2 level rice-cooker cups uncooked Japanese short-grain rice; use a 180 ml rice cup for each cup, 360 ml total
- 400 ml water for the stovetop rice method below
- 1/2 tbsp dashi powder
- 1/2 tbsp light soy sauce, for the rice
- 150 g chicken, sliced
- 1 tsp cornstarch, for the chicken
- 1/2 tsp light soy sauce, for the chicken
- 100 g carrot, finely diced; adjustable from 75 to 150 g
- 100 g corn kernels, drained if canned or thawed if frozen; adjustable from 75 to 150 g
- 100 g cabbage, shredded; adjustable from 75 to 150 g

#### Method

1. Rinse and drain the rice. Put it in a saucepan with 400 ml water, bring to a simmer, cover tightly, and cook over low heat for about 15 minutes. Turn off the heat and leave covered for 10 minutes. Fluff and use while warm. Follow the rice packet's water and timing instructions if they differ. For a rice cooker, use its water line for 2 Japanese-rice cups instead of the stovetop water amount.
2. While the rice cooks, mix the chicken with the cornstarch and its 1/2 tsp soy sauce.
3. Heat half the olive oil over medium heat. Fry the garlic briefly, add the carrot, corn and cabbage, and stir-fry until softened. Transfer to a clean plate.
4. Add the remaining olive oil and fry the chicken until cooked through, reaching 74°C. Transfer it to the plate with the vegetables.
5. Melt the butter in the pan. Add the warm rice, dashi powder and 1/2 tbsp soy sauce. Toss until evenly mixed, then add the cooked chicken and vegetables and heat through. Cook in batches if needed.

#### Notes

- The two rice-cooker cups are retained. A 180 ml rice cup and the stovetop water amount are proposed working measures, not measurements recorded in the source.
- Vegetable choices, quantities and chicken cornstarch are suggested additions. Choose more vegetables for a more vegetable-heavy dish.
- Use the rice promptly after cooking. If preparing ahead, cool it promptly, refrigerate it, and reheat the finished dish to 74°C.
- The source's alternative pork title has no separate pork method, so this version uses chicken.

#### Source

Supplied recipe document.

<a id="pumpkin-rice"></a>

### Pumpkin rice

**ID:** `pumpkin-rice`

**Servings:** 5 portions.

**Time:** About 90 to 120 minutes, including soaking, a 30-minute marinade, one white-rice cooker cycle and a 10-minute rest. Soak and marinate at the same time.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 300 g uncooked jasmine white rice, about 1.5 standard 240 ml measuring cups
- 480 ml total cooking liquid, made from 240 ml unsalted chicken stock, 120 ml strained mushroom soaking water and 120 ml fresh water
- 300 g peeled pumpkin, cut into 3 cm cubes
- 6 medium dried shiitake mushrooms
- 300 ml warm water, for soaking the mushrooms; only 120 ml goes into the rice
- 200 g minced chicken
- 1 tsp soy sauce and 1 tsp sesame oil, for the chicken marinade
- 3 large shallots, thinly sliced
- 4 garlic cloves, minced
- 20 g small dried scallops; use 15 to 30 g for a milder or stronger seafood flavour
- 200 ml warm water, for soaking the scallops; discard after soaking
- 1 tbsp cooking oil
- 1 tbsp oyster sauce
- 1 tbsp soy sauce, for seasoning the rice

#### Method

1. Rinse the mushrooms and soak in 300 ml warm water for 30 to 45 minutes, until soft throughout. Slice them and discard the tough stalks. Strain the soaking water through a fine sieve lined with kitchen paper; measure out 120 ml. If less remains, top it up with fresh water to 120 ml. Separately soak the dried scallops in 200 ml warm water for 45 to 60 minutes, until soft enough to shred. Drain and shred them.
2. Meanwhile, mix the chicken with its 1 tsp soy sauce and 1 tsp sesame oil. Refrigerate for at least 30 minutes. Rinse the rice and drain well for 10 minutes.
3. Heat the cooking oil in a frying pan over medium heat. Fry the shallots for 2 to 3 minutes, then add the garlic, drained scallops and mushrooms. Fry for another minute.
4. Add the chicken and break it into small pieces. Cook for 4 to 6 minutes, until cooked through and 74°C. Stir in the pumpkin, drained rice, oyster sauce and remaining 1 tbsp soy sauce for 1 minute.
5. Transfer to a rice cooker. Mix the 240 ml stock, 120 ml mushroom soaking water and 120 ml fresh water in a jug, then add this entire 480 ml to the cooker. Spread the rice evenly under the liquid. Do not add another 2 cups of water.
6. Run the white-rice cycle, then leave the lid closed for 10 minutes. Check that the grains are tender and the pumpkin pierces easily with a fork. If the rice still has a hard centre, sprinkle over 2 tbsp hot water and run the cooker for another 5 to 10 minutes, following its instructions. Fluff and serve.

#### Notes

- This working version defines the rice as 300 g uncooked white jasmine rice and interprets the liquid as 480 ml total. The stock and mushroom soaking water are part of that total, not extra liquid. Start with 480 ml; on later batches, use 450 to 500 ml total for firmer or softer rice, changing only the fresh-water portion.
- Use a 240 ml measuring cup if measuring by volume. A 180 ml rice-cooker cup is smaller. Weighing the rice avoids that difference.
- This version chooses dried scallops because the original method calls for soaking and shredding them. The weight is a suggested starting amount, not a conversion of the original 6 to 8 scallops.
- The original liquid ratios conflict with its cup quantities. This adaptation replaces those ratios and does not cover brown rice, which needs a different cooking cycle and liquid amount.
- The original quantities make five modest portions. Increase the whole recipe if needed, keeping the same rice-to-liquid ratio and within the cooker's capacity.

#### Source

Supplied recipe document.

- [Original recipe link](https://thedomesticgoddesswannabe.com/2015/07/pumpkin-rice-with-pork-belly-chinese-sausage-and-dried-scallops/)

<a id="tomato-pasta-sauce-bottled"></a>

### Tomato pasta sauce using bottled sauce

**ID:** `tomato-pasta-sauce-bottled`

**Servings:** 5 portions.

**Time:** Suggested: 15 minutes preparation and about 30 to 35 minutes cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 500 g prepared tomato pasta sauce; use 400 to 600 g
- 1 large tomato, diced
- 1 onion, diced
- 4 garlic cloves, minced
- 50 g cauliflower, cut into small florets, optional
- 150 g fresh mushrooms, sliced; use 100 to 200 g
- 300 g minced beef, pork or chicken; choose one
- 1 tbsp olive oil
- 1 tbsp plain yoghurt
- 120 ml milk, as a working amount for the original 1/2 cup
- 50 g shredded mozzarella, optional; use 25 to 75 g
- 400 g dry pasta, for serving; use 375 to 500 g
- Water for boiling the pasta

#### Method

1. Heat the oil in a large pan over medium heat. Fry the onion for about 4 minutes until softened, then add the garlic and tomato and cook for 2 minutes.
2. Add the mince, break up clumps and cook through. Use 71°C for beef or pork mince, or 74°C for chicken. Add the mushrooms and optional cauliflower and cook for about 3 minutes.
3. Stir in the prepared pasta sauce. Cover partly and simmer for about 15 minutes, stirring occasionally, until the cauliflower is tender if used.
4. Meanwhile, cook the pasta in boiling water according to its label. Reserve 250 ml pasta water, then drain.
5. Lower the sauce heat. Stir in the yoghurt, milk and optional cheese and heat gently for the final 2 minutes, without boiling hard.
6. Toss the pasta with the sauce. Add reserved pasta water 1 tbsp at a time if needed to loosen the sauce, then divide among five portions.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- The sauce, mushrooms, cheese and pasta have suggested measured amounts. Use the upper sauce amount with the upper pasta amount. The original 300 g mince is retained.
- Pasta is an added serving component so this entry can make a meal. When using the sauce with a different base, omit the pasta from its shopping list.
- The optional cauliflower now cooks in the sauce. The milk uses a suggested 240 ml household cup.

#### Source

Supplied recipe document.

<a id="tomato-pasta-sauce-homemade"></a>

### Homemade tomato pasta sauce

**ID:** `tomato-pasta-sauce-homemade`

**Servings:** 5 portions.

**Time:** Suggested: 20 minutes preparation and about 35 to 40 minutes cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 2 tomatoes, diced
- 100 g pumpkin, peeled and diced
- 2 apples, peeled, cored and diced
- 1 carrot, diced
- 100 g cauliflower, cut into small florets
- Leaves from 1 sprig basil
- 150 g cooked, drained red lentils, as a working amount for the original 3/4 cup
- 1 tsp Italian herbs
- 1 onion, diced
- 4 garlic cloves, minced
- 150 g fresh mushrooms, sliced; use 100 to 200 g
- 1 tbsp olive oil for the sauce, plus 1 tbsp only if choosing mince
- 300 ml water, plus up to 100 ml more if needed for simmering or blending
- 2 tbsp plain yoghurt
- 120 ml milk, as a working amount for the original 1/2 cup
- 30 g shredded mozzarella, optional; use 20 to 50 g
- 250 g drained silken tofu, cut into pieces; use 200 to 300 g, or use the original alternative of 150 g minced beef, pork or chicken
- 400 g dry pasta, for serving; use 375 to 500 g
- Water for boiling the pasta

#### Method

1. Heat 1 tbsp olive oil in a large saucepan. Fry the onion for about 4 minutes, then add the garlic and cook for 30 seconds. Add the tomatoes, pumpkin, carrot, cauliflower, apples and mushrooms and stir-fry for 3 minutes.
2. Add the Italian herbs and 300 ml water. Bring to a simmer, cover and cook for about 20 minutes, stirring occasionally, until the vegetables and apples are soft. Add up to 100 ml more water if the pan starts to dry out. During the simmer, boil the pasta according to its label. Reserve 250 ml pasta water, drain and keep the pasta ready to combine.
3. Meanwhile, if choosing mince, heat the remaining 1 tbsp oil in a separate frying pan and cook the mince through, breaking up clumps. Use 71°C for beef or pork, or 74°C for chicken. Skip this step if choosing tofu.
4. Stir the cooked lentils and basil into the softened vegetable mixture. Let it cool slightly, then blend with an immersion blender until as smooth as desired. A countertop blender must be suitable for warm liquids and vented according to its instructions.
5. Return the sauce to low heat. Add the tofu or cooked mince, yoghurt, milk and optional cheese. Heat gently for about 3 to 5 minutes, until the tofu is hot throughout if used. Avoid boiling hard.
6. Toss the cooked pasta with enough sauce to coat it, adding reserved water 1 tbsp at a time if needed. Serve any extra sauce alongside or refrigerate it promptly.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- Mushroom, tofu, cheese and pasta amounts are suggested replacements for undefined containers or missing measures. More tofu makes a heartier sauce. Choose tofu or mince, not both.
- Water, oil and a complete simmering method are proposed additions. The source's two apples are retained and make the sauce sweet.
- The cooked-lentil weight and milk volume are working interpretations of the original cup measures. Use cooked lentils as listed, not the same weight of dry lentils.
- Pasta is an added serving component. Omit it from the shopping list when making only the sauce.

#### Source

Supplied recipe document.

<a id="bolognese-pasta"></a>

### Bolognese pasta

**ID:** `bolognese-pasta`

**Servings:** 5 portions.

**Time:** Suggested: about 50 minutes. Simmer sauce for about 30 minutes, until the vegetables are soft.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 400 g dry pasta; adjustable from 375 to 500 g
- 1 tbsp olive oil
- 4 garlic cloves, minced
- 1 large onion, diced
- 1 carrot, finely diced
- 30 g raisins; adjustable from 20 to 50 g
- 1 celery stalk, outer layer removed, finely diced
- 150 g mushrooms, chopped; adjustable from 100 to 200 g
- 1 tbsp Italian herbs
- 1 basil leaf
- 2 large tomatoes, peeled and diced
- 200 g minced beef
- 500 g prepared tomato pasta sauce; adjustable from 400 to 600 g
- 1 tbsp tomato paste, optional; use up to 2 tbsp for a stronger tomato flavour
- 50 g mozzarella, optional; adjustable from 25 to 100 g
- 2 tbsp milk; use up to 3 tbsp
- 1 head broccoli, cut into florets, for serving
- 4 eggs, for serving
- Water for boiling the pasta and eggs, and steaming the broccoli

#### Method

1. Heat the olive oil in a large pan over medium heat. Soften the onion, add the garlic, and fry briefly. Add the minced beef, break up any clumps, and cook through to 71°C. Add the mushrooms and cook until softened.
2. Add the carrot, celery, tomatoes, Italian herbs and basil. Fry until the tomatoes soften.
3. Add the pasta sauce and raisins. Bring to a simmer and cook gently for about 30 minutes, stirring occasionally, until the vegetables are soft. If the sauce becomes too thick, add a little water.
4. Meanwhile, cook the pasta in boiling water according to its packet instructions. Reserve 250 ml of the pasta water, then drain. Steam the broccoli until tender. Boil the eggs until both the whites and yolks are firm, then peel and cut them for sharing across five portions.
5. Stir 2 tbsp milk into the sauce. Taste and add the optional tomato paste for a stronger tomato flavour. Use the remaining 1 tbsp milk if desired, then simmer for another 2 minutes.
6. Toss the cooked pasta with the sauce. Add reserved pasta water 1 tbsp at a time if needed to coat the pasta. Divide among five portions, add the optional mozzarella, and serve with the broccoli and eggs.

#### Notes

- Pasta, mushrooms, sauce, raisins, olive oil and cheese now have suggested amounts. Pair the upper pasta amount with the upper sauce amount. More raisins make the sauce sweeter; more cheese makes it richer.
- The recorded 200 g beef and 4 eggs are retained. Cut the eggs to share across five portions.
- The source calls the eggs half-boiled and gives 8 minutes. This adaptation uses firm whites and yolks instead of promising that one time suits every egg size.
- The method now adds the raisins, cooks the pasta, and explains how to combine them with the sauce.

#### Source

Supplied recipe document.

<a id="creamy-chicken-macaroni-soup"></a>

### Creamy chicken macaroni soup

**ID:** `creamy-chicken-macaroni-soup`

**Servings:** 5 portions.

**Time:** About 40 to 45 minutes, including 10 to 15 minutes of simmering and 3 to 5 minutes to finish the macaroni in the soup.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 100 g fresh brown mushrooms, weighed after trimming, sliced; use 75 to 150 g
- 1/2 medium onion, diced
- 1 medium carrot, cut into 1 cm dice
- 1 celery stick, tough strings removed and stalk diced
- 1 small leek, trimmed, washed between the layers and thinly sliced
- 4 garlic cloves, minced
- 2 boneless chicken breast fillets, cut into 2 cm cubes
- 1 tbsp cooking oil or butter
- 1.25 litres prepared low-salt chicken stock; use 1 to 1.5 litres for a thicker or brothier soup
- 200 ml water, plus up to 250 ml hot water if needed to finish the pasta
- 300 g dry macaroni; use 250 to 350 g for smaller or larger pasta portions
- Water for boiling the macaroni, enough to cover it generously; drain before adding the pasta to the soup
- 150 ml milk

#### Method

1. Heat the oil or butter in a large pot over medium heat. Fry the onion, celery and leek for 3 to 4 minutes. Add the garlic and mushrooms and fry for 2 minutes.
2. Add the carrot, chicken, chosen stock amount and 200 ml water. Bring to a gentle boil, then lower the heat, partially cover and simmer for 10 to 15 minutes. The carrot should be nearly tender and the chicken must reach 74°C.
3. Meanwhile, boil the macaroni in a separate pan of water for 3 minutes less than the packet's cooking time, then drain. If the packet gives a cooking time below 6 minutes, cook for half that time instead.
4. Add the drained macaroni to the soup. Simmer for 3 to 5 minutes, stirring, until the pasta and vegetables are tender. If the pasta needs more time and the soup is becoming too thick, add hot water in 50 ml portions.
5. Turn the heat low, stir in the milk and heat gently for 1 to 2 minutes, until hot throughout. Avoid a hard boil after adding the milk. Serve immediately.

#### Notes

- The stock quantity means ready-to-use stock, including any water used to dilute concentrate according to its label. It does not mean an entire packet of stock powder or undiluted concentrate.
- The default broth starts with 1.25 litres stock, 200 ml water and 150 ml milk, or 1.6 litres before evaporation and pasta absorption. Choose 1 litre stock for a thicker soup or 1.5 litres for more broth.
- Mushroom and macaroni weights are suggested amounts. The supplied two chicken fillets and 150 ml milk are retained.
- For make-ahead meals, cook the macaroni fully and store it separately from the soup so it does not absorb all the broth. Cool and refrigerate promptly. Reheat the soup and pasta together to 74°C, adding water as needed.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.instagram.com/reel/C8T2t_3Svcs/)

<a id="japanese-sushi-onigiri"></a>

### Japanese sushi and onigiri

**ID:** `japanese-sushi-onigiri`

**Servings:** 5 portions.

**Time:** Suggested: about 50 minutes including rice cooking; fillings can cook while the rice rests.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

**Salmon filling**

- 600 g boneless salmon
- 2 tsp sesame oil
- 1 1/2 carrots, shredded
- 1 1/2 zucchini, shredded
- 100 g ready-cooked crab sticks, sliced; use 75 to 150 g
- 1 tsp soy sauce
- 30 g cream cheese, softened; use 20 to 50 g
- 3 tbsp Greek yoghurt
- 1 1/2 tsp mayonnaise

**Scrambled eggs**

- 4 eggs
- 1 tsp soy sauce
- 1/2 tsp dashi powder
- 1 tsp mirin
- 1 tsp water
- 1 tsp neutral cooking oil

**Rice and serving**

- 225 g dry Japanese short-grain rice, as a suggested replacement for the unclear 1 1/2 cups
- 300 ml water for the rice, or the amount specified by the rice label
- 10 g furikake; use 5 to 15 g
- 1 1/2 tbsp apple cider vinegar
- 1 1/2 tbsp non-alcoholic mirin
- 5 full-size nori sheets, halved for hand rolls or cut into strips for rice balls
- 30 g pork floss, optional; use 20 to 50 g

#### Method

1. Rinse and drain the rice. Put it in a saucepan with 300 ml water, bring to a simmer, cover and cook over low heat for about 15 minutes. Turn off the heat and leave covered for 10 minutes. Follow the rice label's water and timing instructions if they differ.
2. Meanwhile, heat the oven to 180°C. Coat the salmon with its sesame oil and bake on a lined tray. Start checking after 10 minutes and continue until its thickest part reaches 63°C. Flake it and check carefully for bones.
3. Steam the carrots for about 5 minutes and the zucchini for about 3 minutes, until just tender. Heat the ready-cooked crab sticks according to their label. Drain and gently press excess moisture from the vegetables. Mix them with the salmon, crab sticks, filling soy sauce, cream cheese, yoghurt and mayonnaise.
4. Beat the eggs with their soy sauce, dashi powder, mirin and water. Heat the neutral oil in a non-stick pan and scramble the mixture over medium-low heat until set and at least 71°C.
5. Mix the warm rice with the furikake, vinegar and non-alcoholic mirin. Let it cool just enough to handle. Divide the rice, salmon mixture and eggs into five equal meal portions.
6. For hand rolls, give each portion two nori halves. Spread a thin layer of rice over one end, add a little salmon mixture and egg, then roll into a cone and eat promptly. Serve filling that does not fit alongside; do not overfill.
7. For onigiri instead, shape each rice portion into two small balls with clean damp hands. Make an indentation, add about 1 tsp salmon filling, close the rice around it and wrap with a nori strip. Serve the remaining filling and scrambled egg alongside. Add the optional pork floss to either serving style.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- Crab sticks, cream cheese and furikake now have measured working amounts. More furikake makes the rice more strongly seasoned; start with 5 g if the blend is salty.
- The original rice cups did not specify cooked or dry. This adaptation proposes 225 g dry rice rather than claiming to recover that amount. The five portions have modest rice and generous filling; serve excess filling alongside the rolls or rice balls.
- Rice cooking, egg cooking and both assembly options are proposed completions. Nori and optional pork-floss amounts are suggested.
- Eat promptly or refrigerate leftovers promptly. Do not leave cooked rice or fish at room temperature for extended assembly.

#### Source

Supplied recipe document.

<a id="korean-kimbap"></a>

### Korean kimbap

**ID:** `korean-kimbap`

**Servings:** 5 portions.

**Time:** Suggested: about 30 minutes using ready-cooked rice; prepare the fillings while heating the rice.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 150 g plain ready-cooked mixed-grain rice
- 300 g plain ready-cooked Japanese short-grain rice
- 1 tbsp sesame oil
- 1 tsp ground toasted sesame seeds; use up to 2 tsp
- 3 small sheets Korean salted seaweed, crumbled into the rice
- 150 g canned tuna, drained weight; use 120 to 200 g
- 1/2 carrot, shredded
- 75 g cooked sweetcorn kernels; use 50 to 100 g
- 1 hard-boiled egg, chopped, optional
- 1 tsp soy sauce
- 2 tbsp Greek yoghurt
- 1 tsp mayonnaise
- 3 full-size unseasoned nori sheets, for rolling

#### Method

1. Heat the ready-cooked rice according to its label until steaming hot. If using freshly cooked rice instead, weigh 150 g mixed-grain and 300 g Japanese rice after cooking. Combine them while warm and mix in the sesame oil, ground sesame and crumbled Korean salted seaweed. Let cool just enough to handle.
2. Steam the shredded carrot for about 5 minutes, until tender, then drain well. Drain the tuna thoroughly and mix it with the carrot, cooked corn, optional chopped hard-boiled egg, soy sauce, yoghurt and mayonnaise.
3. Place a full-size nori sheet shiny-side down on a rolling mat. Spread one-third of the rice thinly over the lower two-thirds of the sheet. Place a narrow line of filling across the rice about 3 cm from the bottom edge.
4. Roll firmly from the bottom, using the mat to keep the filling together. Dampen the bare top edge with a little water to seal. Repeat with the other sheets and rice. Serve any filling that does not fit alongside rather than overfilling the rolls.
5. Cut each roll into bite-sized slices with a damp knife and divide the rolls and any extra filling among five portions. Eat promptly, or refrigerate promptly until serving.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- The tuna uses drained grams rather than an unknown can. Corn and sesame now have suggested working amounts. More tuna makes a fish-heavy filling; more corn makes it sweeter.
- The original rice cups did not specify cooked or dry. The 150 g and 300 g cooked weights are proposed replacements that keep the recorded one-to-two grain ratio. Ready-cooked rice gives a definite purchase amount without assuming a water ratio for an unspecified grain blend. Do not use these weights for dry rice.
- The three small salted seaweed sheets season the rice. Three full-size nori sheets are a proposed separate ingredient for rolling. These make five small shared-dish portions.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.instagram.com/reel/C6GjWiwLOMb/)

<a id="mexican-wraps"></a>

### Mexican wraps

**ID:** `mexican-wraps`

**Servings:** 5 portions.

**Time:** Suggested: 25 minutes preparation and about 25 minutes cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

**Beef filling**

- 400 g fresh minced beef
- 1 onion, finely diced
- 2 garlic cloves, minced
- 2 tbsp tomato paste
- 50 ml water
- 1/8 tsp black pepper
- 1 tsp all-purpose seasoning, or 1 tsp paprika plus 1 tsp mushroom salt
- 1 tsp oregano or Italian herbs
- 1 tsp garlic powder
- 1 tsp onion powder
- 1 tbsp oil
- 75 g grated cheddar or mozzarella, for baking; use 50 to 100 g

**Tofu scrambled eggs**

- 6 eggs
- 150 g silken tofu, drained; use 100 to 200 g
- 30 g grated mozzarella; use 20 to 50 g
- 1/8 tsp salt
- 1 tbsp milk
- 10 g butter

**Guacamole**

- 1 avocado
- 2 tbsp Greek yoghurt
- Juice of 1/2 lime
- 1/8 tsp salt
- 1 tsp garlic powder
- 1 small shallot, finely chopped
- 100 g cherry tomatoes, diced; use 75 to 150 g

**To serve**

- 5 medium soft wraps, about 25 cm across, or 10 hard-shell tacos
- 100 g shredded carrot; use 75 to 150 g
- 75 g mesclun salad; use 50 to 100 g
- 250 g frozen fish fingers, optional; use 200 to 300 g

#### Method

1. Heat the oven to 180°C. If using the optional fish fingers, cook them on a separate tray according to their label's temperature and timing; adjust the oven between components if needed. Keep them hot for serving.
2. Heat the oil in a frying pan. Fry the onion for about 4 minutes, then add the garlic and fry for 30 seconds. Add the beef and cook, breaking up clumps, until it reaches 71°C.
3. Stir in the pepper, chosen all-purpose seasoning or paprika-and-mushroom-salt alternative, herbs, garlic powder and onion powder. Add the tomato paste and water. Simmer for 2 to 3 minutes until the filling is moist but not watery.
4. Transfer the cooked beef to a shallow ovenproof dish. Scatter the baking cheese over it and bake at 180°C for about 8 minutes, until melted. The cheese is baked on the beef, before assembly.
5. Beat the eggs with the milk and salt. Melt the butter in a non-stick pan over medium-low heat, add the drained tofu and break it into small pieces. Add the eggs and stir gently until set and at least 71°C. Fold in the mozzarella and remove from the heat once melted.
6. Mash the avocado with the yoghurt, lime juice, salt and garlic powder. Stir in the shallot and diced tomatoes to make the guacamole.
7. Warm the wraps or taco shells according to their label. Divide the beef, eggs, guacamole, carrot and salad among five servings, with fish fingers if chosen. Fill each wrap modestly, fold in the sides and roll, or spoon filling into the taco shells. Serve excess filling alongside rather than overfilling.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- Tofu and tomato weights replace undefined half-packets. Cheese, butter, salad and serving-base amounts are proposed. Use less tofu or cheese for lighter eggs, or more for a larger filling.
- Choose soft wraps or hard-shell tacos. Fish fingers are optional and use their own product cooking instructions; they are not assumed to cook during the beef's 8-minute cheese bake.
- This is a generous shared meal with several fillings. The original 400 g beef and six eggs are retained; divide everything among five portions and serve filling that does not fit alongside.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.recipetineats.com/ground-beef-tacos-recipe/#recipe)

## For kids

<a id="yoghurt-pancakes"></a>

### Yoghurt pancakes

**ID:** `yoghurt-pancakes`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 6 tbsp flour
- 1 tsp baking powder
- 1 egg, beaten
- 5 tbsp strawberry yoghurt
- 3 tbsp mashed banana; defrost before mashing if frozen
- 1 drop vanilla essence

#### Method

1. Mix the ingredients and fry in a pan until fluffy.

#### Source

Supplied recipe document.

<a id="baked-salmon-sweet-potato-nuggets"></a>

### Baked salmon and sweet potato nuggets

**ID:** `baked-salmon-sweet-potato-nuggets`

**Servings:** 5 portions.

**Time:** Salmon: bake for 8 minutes. Sweet potato: microwave for 7 minutes. Other vegetables: microwave for 3 minutes. Final bake: 30 minutes.

**Review:** Imported draft.

#### Ingredients

- 200 g salmon
- Herbs, types and quantities not specified
- 1 sweet potato, peeled
- 3 broccoli stalks
- Grated carrot or zucchini, water squeezed out; quantity not specified
- 1 egg
- 1/4 cup "oat or wholemeal flour", as written in the source

#### Method

1. Bake the salmon with herbs at 180°C for 8 minutes.
2. Microwave the peeled sweet potato for 7 minutes. Microwave the broccoli and grated carrot or zucchini for 3 minutes. Blend the cooked vegetables.
3. Mix the salmon, blended vegetables, and the stated oat or wholemeal flour well. The oat form is unclear. The egg is listed in the source but its addition is not stated.
4. Bake for 30 minutes at 180°C.

#### Notes

- Microwave power is not specified.
- The source lists 1 egg without an explicit addition step. The amount of carrot or zucchini and the nugget shaping method are not provided. Confirm whether "oat" means oats or oat flour.

#### Source

Supplied recipe document.

<a id="tofu-meatballs"></a>

### Tofu meatballs

**ID:** `tofu-meatballs`

**Servings:** 5 portions.

**Time:** Bake: 20 minutes. Pan-fry: 3 minutes per side, or until slightly browned.

**Review:** Imported draft.

#### Ingredients

- 200 g minced chicken or pork
- 100 g silken tofu
- 1/2 medium onion, diced
- 1/2 tsp garlic powder
- 1/2 carrot
- 1/2 zucchini, grated and drained, or 3 to 4 broccoli stalks
- 1 egg
- 5 tbsp breadcrumbs; applicability unclear, see Notes
- 5 tbsp shredded mozzarella; applicability unclear, see Notes
- Salt, a sprinkle; applicability unclear, see Notes

#### Method

1. Roll into balls and bake for 20 minutes at 180°C.
2. Remove from the oven and pan-fry both sides for 3 minutes per side, or until slightly browned.

#### Notes

- A personal note in the source appears immediately before the breadcrumbs, mozzarella, and salt. Names were removed. Confirm whether these ingredients describe a separate variation and whether the following method applies to all variations.
- The method changes the description from balls to nuggets. Shape is not otherwise specified.
- The source gives no explicit mixing step.

#### Source

Supplied recipe document.

<a id="fish-pumpkin-scallop-porridge"></a>

### Fish, pumpkin, and scallop porridge

**ID:** `fish-pumpkin-scallop-porridge`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 4 tbsp rice
- Fish, quantity not specified
- Ginger, quantity not specified
- Pumpkin, quantity not specified
- Scallops, quantity and form not specified
- Snow peas, for a steamed side; quantity not specified

#### Method

1. Steam the snow peas to serve alongside the porridge. Porridge cooking instructions are not specified in the source.

#### Notes

- This entry preserves one of the source's porridge combinations. Liquid quantity and cooking time are not specified.

#### Source

Supplied recipe document.

<a id="fish-wolfberry-carrot-porridge"></a>

### Fish, wolfberry, and carrot porridge

**ID:** `fish-wolfberry-carrot-porridge`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 4 tbsp rice
- Fish, quantity not specified
- Ginger, quantity not specified
- Wolfberries, quantity not specified
- Carrot, quantity not specified
- Cauliflower, for a steamed side; quantity not specified

#### Method

1. Steam the cauliflower to serve alongside the porridge. Porridge cooking instructions are not specified in the source.

#### Notes

- This entry preserves one of the source's porridge combinations. Liquid quantity and cooking time are not specified.

#### Source

Supplied recipe document.

<a id="minced-pork-carrot-porridge"></a>

### Minced pork and carrot porridge

**ID:** `minced-pork-carrot-porridge`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 4 tbsp rice
- Minced pork, quantity not specified
- Sesame oil, for marinating the pork; quantity not specified
- Corn flour, for marinating the pork; quantity not specified
- Garlic powder, quantity not specified
- Onion, quantity not specified
- Carrot, quantity not specified
- Broccoli, for a steamed side; quantity not specified

#### Method

1. Marinate the minced pork with sesame oil and corn flour. Steam the broccoli as a side. Porridge cooking instructions are not specified in the source.

#### Notes

- This entry preserves one of the source's porridge combinations. Liquid quantity and cooking time are not specified.

#### Source

Supplied recipe document.

<a id="minced-chicken-vegetable-porridge"></a>

### Minced chicken and vegetable porridge

**ID:** `minced-chicken-vegetable-porridge`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 4 tbsp rice
- Minced chicken, quantity not specified
- Corn flour, for marinating the chicken; quantity not specified
- Olive oil, for marinating the chicken; quantity not specified
- Celery or zucchini, quantity not specified
- Carrot, quantity not specified

#### Method

1. Marinate the minced chicken with corn flour and olive oil. Porridge cooking instructions are not specified in the source.

#### Notes

- This entry preserves one of the source's porridge combinations. Liquid quantity and cooking time are not specified.

#### Source

Supplied recipe document.

<a id="beef-sweet-potato-porridge"></a>

### Beef and sweet potato porridge

**ID:** `beef-sweet-potato-porridge`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 4 tbsp rice
- Beef, quantity not specified
- Carrot, quantity not specified
- Sweet potato, quantity not specified
- Onion, quantity not specified
- Tofu, optional; quantity not specified

#### Method

Not specified in source.

#### Notes

- This entry preserves one of the source's porridge combinations. Liquid quantity and cooking time are not specified.

#### Source

Supplied recipe document.

<a id="chicken-drumstick-soup-carrot-leek-potato"></a>

### Chicken drumstick soup with carrot, leek, and potato

**ID:** `chicken-drumstick-soup-carrot-leek-potato`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Carrot, quantity not specified
- Leek, quantity not specified
- Potato, quantity not specified
- Chicken drumstick, quantity not specified

#### Method

Not specified in source.

#### Notes

- The source contains only this ingredient combination. Stock or water quantity and cooking instructions are not specified.

#### Source

Supplied recipe document.

<a id="chicken-drumstick-soup-carrot-potato-tomato"></a>

### Chicken drumstick soup with carrot, potato, and tomato

**ID:** `chicken-drumstick-soup-carrot-potato-tomato`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Carrot, quantity not specified
- Potato, quantity not specified
- Onion, quantity not specified
- Tomato, quantity not specified
- Chicken drumstick, quantity not specified

#### Method

Not specified in source.

#### Notes

- The source contains only this ingredient combination. Stock or water quantity and cooking instructions are not specified.

#### Source

Supplied recipe document.

<a id="chicken-rice-cauliflower"></a>

### Chicken rice with cauliflower

**ID:** `chicken-rice-cauliflower`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Minced chicken, pounded until soft; quantity not specified
- 1/2 tsp "chicken (no salt)", as written in the source; ingredient form unclear
- 1/2 tsp mushroom powder
- Onion, quantity not specified
- Garlic powder, quantity not specified
- 1/2 tsp sesame oil
- 4 tbsp Japanese rice
- 6 tbsp water, marked with a question mark in the source
- Cauliflower, named in the title; quantity not specified

#### Method

Not specified in source.

#### Notes

- Confirm the water quantity, which the source marks as uncertain, and the identity of the "chicken (no salt)" seasoning. Cauliflower appears only in the title. No cooking method or time is supplied.

#### Source

Supplied recipe document.

<a id="fried-rice-kids"></a>

### Fried rice for kids

**ID:** `fried-rice-kids`

**Servings:** 5 portions.

**Time:** Suggested: about 25 minutes with cooked, chilled rice.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 800 g cooked, chilled rice; adjustable from 750 to 1,000 g
- 200 g minced chicken; adjustable from 150 to 250 g
- 1/2 tsp cornstarch, for the chicken
- 1 tsp sesame oil, for the chicken
- 3 garlic cloves, minced; adjustable from 2 to 4 cloves
- 1 small shallot, minced; adjustable from 1 to 2 shallots
- 100 g carrot, shredded; adjustable from 100 to 150 g
- 200 g cabbage, shredded; adjustable from 150 to 250 g
- 1 egg, beaten
- 1 tsp light soy sauce
- 1 tbsp neutral cooking oil, divided

#### Method

1. Mix the chicken with the cornstarch and sesame oil. Break up any clumps in the chilled rice.
2. Heat half the cooking oil in a large frying pan over medium heat. Scramble the egg until set, then transfer it to a clean plate.
3. Add the remaining oil and the chicken. Break the chicken into small pieces and stir-fry until cooked through, reaching 74°C. Transfer it to the plate with the cooked egg.
4. Fry the garlic and shallot in the same pan for about 30 seconds, then add the carrot and cabbage. Stir-fry until the vegetables soften.
5. Add the rice and stir-fry until hot throughout. Return the cooked chicken and egg, add the soy sauce, and toss until evenly mixed and reheated to 74°C. Use two batches if the pan is crowded.

#### Notes

- The rice amount is a suggested five-portion working quantity, not a conversion of the source's undefined six scoops. Use the lower end for smaller appetites or when serving other dishes.
- The chicken, vegetables, aromatics and cooking oil now have suggested amounts. Light soy sauce replaces the source's unspecified sauce formulation.
- Use rice that was cooled promptly and refrigerated. Do not leave cooked rice at room temperature overnight.

#### Source

Supplied recipe document.

## Archive

<a id="tomato-egg-soup-mee-sua"></a>

### Tomato egg soup with mee sua

**ID:** `tomato-egg-soup-mee-sua`

**Servings:** 5 portions.

**Time:** Suggested: 20 minutes preparation and about 25 minutes cooking.

**Review:** Adapted draft. Suggested quantities and method; not kitchen-tested.

#### Ingredients

- 5 large tomatoes, diced
- 2 garlic cloves, minced
- 4 eggs, beaten
- 1 large shallot, finely chopped
- 1 litre prepared chicken stock
- White parts of 2 spring onions, sliced
- 250 g boneless firm white fish, such as cod or sea bass, sliced about 1 cm thick
- 1 tsp light soy sauce, for the fish
- 1 tsp cornstarch, for the fish
- 1 tsp sesame oil, for the fish
- 100 g cooked sweetcorn kernels; use 75 to 150 g
- 150 g fresh mushrooms, trimmed and sliced; use 100 to 200 g
- 250 g leafy vegetables such as bok choy, stems and leaves separated; use 200 to 350 g
- 250 g dry mee sua or soya mee; use 200 to 300 g
- 300 g silken tofu, drained and cubed; use 250 to 400 g
- 1 tbsp neutral cooking oil
- 500 ml water to dilute the stock; add up to 250 ml more if a thinner soup is preferred
- Water for cooking the noodles
- 1 tbsp oyster sauce and 1 tbsp ketchup, optional after tasting

#### Method

1. Coat the fish with its soy sauce, cornstarch and sesame oil. Keep chilled while preparing the soup.
2. Heat the cooking oil in a large pot. Fry the garlic, shallot and spring-onion whites for about 1 minute. Add the tomatoes and cook for about 8 minutes, stirring, until they soften and begin to break down.
3. Add the 1 litre stock, 500 ml water and mushrooms. Bring to a simmer and cook for 5 minutes. Taste, then add the optional oyster sauce and ketchup only if desired.
4. Add the vegetable stems, cooked corn and tofu. Simmer for about 3 minutes. Add the fish and vegetable leaves and simmer gently for about 3 to 5 minutes, until the fish reaches 63°C and the vegetables are tender.
5. Pour in the beaten eggs in a thin stream while stirring gently. Continue simmering until the egg is set and the soup reaches at least 71°C. Add up to 250 ml more water if a thinner soup is preferred, then return to a simmer.
6. Cook the chosen noodles separately according to their label and drain. Divide the noodles among five bowls and ladle over the hot soup and toppings. Serve promptly so the noodles do not soften excessively.

#### Notes

- Suggested quantities and added steps are working adaptations for five portions, not recovered packet measurements. They have not been kitchen-tested.
- This recipe remains in Archive and is not a planning default. Its archived status is unchanged.
- Mushroom, vegetable, tofu, corn and dry-noodle amounts are proposed replacements for packets, a box, a bowl and bundles. More noodles make a fuller bowl; less leaves more room for broth and toppings.
- The source's 1 litre stock is retained. An additional 500 ml water is a proposed addition for five bowls, with up to 250 ml more for preference. Noodles cook separately so they do not absorb this broth before serving.
- Fish type, spring onion, cornstarch, cooking oil and the missing cooking steps are suggested completions.

#### Source

Supplied recipe document.
