# Chef Bob reference recipes

104 recipe entries and variants, including incomplete recipe notes. Imported on **3 October 2026** from the maintainer's recipe collection, last modified **26 August 2026**.

All recipes below use a **5-portion base**. See [portions and scaling](#portions-and-scaling) to adjust them.

For a first plan, start with the six complete [starter recipes](recipes/STARTER_RECIPES.md). Use the index below to browse this larger collection. Ask Chef Bob to show a dish or category in plain language. The [command guide](COMMANDS.md) explains `/help`, `/plan`, `/preferences`, and `/recipe-add`.

## How to use this collection

- Entries marked **Imported draft** have been formatted consistently but still contain source gaps. Missing values are **Not specified**, and conflicts appear under **Notes**. Clarify missing information before using a recipe for a detailed shopping list or cooking instructions.
- Ingredients, quantities, methods, variants, and attribution links have been preserved. Ingredient amounts have not been guessed. External source pages have not been independently re-imported or checked.
- Some oven temperatures only say "degrees"; the scale is unresolved. Bowl, packet, scoop, or bottle sizes also need clarification in many entries.
- Recipe ingredients are independent of household preferences. Apply allergies, exclusions, and substitutions when planning rather than deleting ingredients from the shared collection.
- `/recipe-add` saves additions in your private data directory. It does not publish them or edit this shared file. Contribute a reviewed recipe through the [contribution process](CONTRIBUTING.md) when you want to share it.
- The preparation notes and archived recipe are retained as source material for review. They are not approved planning defaults.

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

Follow recipe-specific scaling notes first. The [ginger soy fish sauce](#ginger-soy-baked-salmon), for example, should not be doubled automatically. Cooking times and temperatures do not scale with portions; check the batch size and method separately. Missing quantities and undefined bowl, packet, or scoop sizes still need clarification.

You can ask Bob:

```text
Use RECIPES.md to plan dinners for 3 portions. Its recipes are based on
5 portions, so scale the listed quantities by 0.6. Follow any recipe-specific
scaling notes, apply my food preferences, and flag missing measurements.
```

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
- [Honey-baked miso halibut](#honey-baked-miso-halibut)
- [Steamed halibut with garlic and ginger sauce](#steamed-halibut-garlic-ginger)
- [Tomato egg](#tomato-egg)
- [Fried egg with shallots and spring onion](#fried-egg-shallots-spring-onion)
- [Baked tomato fish in foil](#baked-tomato-fish-foil)
- [Baked salmon with teriyaki sauce](#baked-salmon-teriyaki)
- [Ginger soy fish with baked salmon](#ginger-soy-baked-salmon)
- [Japanese creamy fish stew](#japanese-creamy-fish-stew)
- [Sweet and sour fried tofu or fish](#sweet-sour-fried-tofu-fish)

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
2. Coat the fish bones with olive oil and bake for 25 minutes at 225 degrees. The temperature scale is not specified.
3. Simmer the fish bones with the chicken bones, yellow soybeans, carrots, onion, coriander root and anchovies for 4 hours.
4. Marinate the sliced fish with the fish seasoning, sesame oil and ginger juice.
5. The source says to serve with spinach/cabbage noodles, eggs and the marinated sliced fish. It does not provide the final cooking steps for these ingredients.

#### Notes

Confirm the ginger amount, water quantity and temperature scale before cooking. Pumpkin appears in the ingredient list but has no method step. "Spinach/cabbage noodles" is ambiguous. The final cooking method for the sliced fish and eggs is missing; this is an incomplete method.

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

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Silken tofu, quantity not specified
- Golden mushrooms, quantity not specified
- 1 cup kimchi
- 1 cheese, unit not specified (optional)

**Broth**

- 1000 ml broth
- Onion, quantity not specified
- Kombu or a dashi pack, quantity not specified
- Leek, quantity not specified
- 1 packet bonito flakes

**Seasoning**

- 3 garlic cloves, minced
- 1 tbsp mirin
- 2 tbsp gochujang
- 1/2 tbsp oyster sauce
- 1 tbsp sesame oil
- 1 tbsp gochugaru (optional, for more spice)
- 2-3 tbsp ketchup or 1 can baked beans

**To serve**

- Korean ramen or rice, quantity not specified

#### Method

1. Prepare the broth by boiling it with onion, kombu or a dashi pack, leek and bonito flakes.
2. Add the seasoning, taste and adjust.
3. Add the remaining stew ingredients.
4. Serve with Korean ramen or rice.

#### Notes

The amount and form of cheese, packet/can sizes, cooking duration and finishing steps for the stew ingredients are not specified.

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
- 3 garlic, sliced; unit not specified
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

The source does not say when to return the broccoli, how to add the optional black fungus, or how long to cook the eggs. The garlic unit and final cooking duration are missing.

#### Source

Supplied recipe document.

<a id="mixed-vegetables"></a>

### Mixed vegetables

**ID:** `mixed-vegetables`

**Servings:** 5 portions.

**Time:** Tossing: 1 minute. Simmering: 2-3 minutes.

**Review:** Imported draft.

#### Ingredients


**Choose up to four main ingredients**

- 1/2 broccoli or 1 small broccoli
- 1/2 cauliflower
- 1/2 packet baby corn, halved
- 1/2 carrot, thinly sliced
- 1/2 packet shimeiji mushrooms
- 1 tau kwa (optional)

**Aromatics**

- 4 slices ginger
- 2 garlic, minced; unit not specified

**Seasoning**

- 100 ml water
- 1 tsp oyster sauce
- 1 tbsp wolfberries
- 1 tsp light soy sauce

**Slurry**

- 3/4 tsp cornstarch
- 1 tbsp water

#### Method

1. Saute the ginger and garlic until fragrant.
2. Add the selected main ingredients and toss for 1 minute.
3. Add the seasoning and simmer for 2-3 minutes.
4. Mix the cornstarch with its water. Slowly pour in the mixture, stirring continuously, to thicken the sauce.

#### Notes

Packet sizes and the unit for garlic are not specified.

#### Source

- [Original source](https://cookwithmi.wixsite.com/cookwithmi/post/cookwithmi-claypot-egg-tofu-with-assorted-vegetables)

<a id="chinese-yam-or-lotus-root-with-mixed-vegetables"></a>

### Chinese yam or lotus root with mixed vegetables

**ID:** `chinese-yam-or-lotus-root-with-mixed-vegetables`

**Servings:** 5 portions.

**Time:** Chinese yam boiling: 3 minutes, or lotus root boiling: 5 minutes.

**Review:** Imported draft.

#### Ingredients

- 1/2 broccoli
- 1/2 carrot, sliced
- 1/2 packet snow peas
- 1/2 Chinese yam, sliced, or 1 lotus root, sliced
- 2 celery sticks, sliced
- 1/2 packet black fungus
- 1/2 cup cashew nuts, toasted
- 1 knob ginger (4 slices)
- 1 tsp minced garlic
- 1 tbsp sesame oil, from the method

**Sauce**

- 1 1/2 tbsp oyster sauce or abalone sauce
- 1/2 cup water
- 1 tbsp wolfberries or 1/2 tsp sugar

#### Method

1. Peel the outer layer from the celery, slice diagonally and soak in water for a while.
2. Boil the Chinese yam for 3 minutes, or the lotus root for 5 minutes.
3. Fry the ginger and garlic. Add the vegetables, adding the snow peas and black fungus last.
4. Add the sesame oil and sauce.
5. Stir in the cashew nuts when ready to serve.

#### Notes

Packet sizes, the form of black fungus, celery soaking time and final stir-frying duration are not specified.

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

**Time:** Simmering: 10-15 minutes.

**Review:** Imported draft.

#### Ingredients

- 1/2 large napa cabbage, cut into strips
- 1/2 carrot, grated or cut into strips
- 3 large dried mushrooms, soaked and thinly sliced
- 2 garlic cloves, minced
- 1 tsp small shrimp, soaked, smashed and finely chopped
- 100 ml mushroom soaking liquid, from the method
- 1/2 tsp oyster sauce, from the method

#### Method

1. Stir-fry the garlic and shrimp until fragrant.
2. Add the cabbage, carrot and mushrooms.
3. Add the mushroom soaking liquid and oyster sauce.
4. Simmer for 10-15 minutes or until the carrot is soft.

#### Notes

The source does not specify the mushroom or shrimp soaking duration.

#### Source

Supplied recipe document.

<a id="roasted-cabbage"></a>

### Roasted cabbage

**ID:** `roasted-cabbage`

**Servings:** 5 portions.

**Time:** Roasting: 20 minutes.

**Review:** Imported draft.

#### Ingredients

- 1/2 large cabbage, cut into wedges
- 1/2 packet oyster and shimeiji mushrooms, washed and squeezed dry
- Salt, quantity not specified, from the method

**Sauce**

- 1 garlic, minced; unit not specified
- Small piece of ginger, minced; size not specified
- 1 tbsp butter
- 1/2 tsp garlic powder
- 1 1/2 tbsp miso
- 60-80 ml water
- 30 ml cream or fresh milk

#### Method

1. Lightly salt the cabbage and mushrooms. Roast for 20 minutes at 180 degrees; the temperature scale is not specified.
2. Lightly fry the garlic and ginger in the butter.
3. Add the mushrooms and garlic powder.
4. Mix the miso with the water and add it, followed by the cream or milk.
5. Taste and adjust before serving.

#### Notes

Confirm the oven temperature scale before cooking. The source appears to use the mushrooms in both roasting and sauce steps but does not clarify how to divide or transfer them. The garlic unit and packet size are not specified.

#### Source

Supplied recipe document.

<a id="stir-fried-bok-choy-with-eggs"></a>

### Stir-fried bok choy with eggs

**ID:** `stir-fried-bok-choy-with-eggs`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 1 bundle bok choy
- 4 eggs
- 1/2 tsp fish sauce
- A little white pepper
- 1 tbsp oyster sauce
- 2 garlic, sliced; unit not specified
- 8 cherry tomatoes, halved
- Baby corn, quantity not specified

#### Method

1. Mix the eggs with the fish sauce and white pepper.
2. Stir-fry the eggs and set aside.
3. Stir-fry the garlic, then add the bok choy stems and cook until half cooked.
4. Add the leaves, cherry tomatoes, baby corn and oyster sauce.
5. Return the eggs and stir-fry for a while.

#### Notes

The source does not specify the garlic unit, baby-corn amount or cooking durations.

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

**Time:** Bitter-gourd soaking: 30 minutes.

**Review:** Imported draft.

#### Ingredients

- 1 bitter gourd (200 g), seeded and thinly sliced
- 3 eggs
- 3 garlic cloves, minced
- 1 small onion, thinly sliced
- 1 block tau kwa, cut into cubes
- 1 tbsp mirin
- 1/4 tsp salt, for sprinkling

**Source soaking mixture**

- Rice water, enough to cover the bitter gourd
- 1 tsp salt
- 1 tsp sugar

**To finish**

- A little cooking oil
- Bonito flakes, quantity not specified

#### Method

1. Soak the bitter gourd in rice water with the 1 tsp salt and sugar for 30 minutes. Discard the water and rinse the bitter gourd.
2. Fry the tau kwa in a little oil until brown, then set aside.
3. Fry the garlic and onion. Add the bitter gourd and mirin.
4. When the vegetables soften, add the tau kwa, followed by the eggs.
5. Serve with bonito flakes.

#### Notes

The source does not say when to add the 1/4 tsp sprinkling salt or how long to cook the eggs. The rice-water soaking instruction is retained from the source for review.

#### Source

- [Original source](https://www.instagram.com/reel/C36k5hcS6Fu/)

<a id="steamed-okra"></a>

### Steamed okra

**ID:** `steamed-okra`

**Servings:** 5 portions.

**Time:** Steaming: 8 minutes.

**Review:** Imported draft.

#### Ingredients

- 1 packet okra (lady's fingers)
- 1 packet bonito flakes, for seasoning A

**Seasoning A**

- 1 tsp dashi powder
- 1 tsp soy sauce
- 1 tbsp mirin
- 2 tbsp sesame seeds

**Seasoning B**

- 1 tbsp soy sauce
- 1 tbsp water
- 1/2 tsp sugar
- 2 tsp sesame oil

#### Method

1. Steam the okra for 8 minutes.
2. Choose seasoning A with the bonito flakes, or seasoning B. Pour the chosen seasoning over the okra before serving.

#### Notes

Choose one seasoning variant. Packet sizes are not specified.

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
- 1 garlic, sliced; unit not specified
- 1 tbsp wolfberries
- 1 tbsp dried scallops
- 1 cup water, from the method

#### Method

1. Steam the spinach for 5 minutes.
2. Stir-fry the garlic until fragrant.
3. Add the water and the remaining broth ingredients. Simmer for 15 minutes.
4. Pour the broth over the spinach and serve.

#### Notes

The source does not specify whether the whitebait is fresh or dried, the garlic unit, the cup size or preparation of the dried scallops.

#### Source

Supplied recipe document.

<a id="japanese-stir-fried-lotus-root-and-tau-kwa"></a>

### Japanese stir-fried lotus root and tau kwa

**ID:** `japanese-stir-fried-lotus-root-and-tau-kwa`

**Servings:** 5 portions.

**Time:** Lotus-root steaming: 10 minutes.

**Review:** Imported draft.

#### Ingredients

- 1 section lotus root, thinly sliced
- 1 tau kwa
- 1 tbsp sesame oil, from the method

**Seasoning**

- 1 tbsp mirin
- 1 tbsp sake
- 1 1/2 tbsp soy sauce
- 1 tbsp water

**To finish**

- Toasted sesame seeds, quantity not specified
- Spring onion, quantity not specified

#### Method

1. Steam the thinly sliced lotus root for 10 minutes.
2. Heat the sesame oil and stir-fry the lotus root and tau kwa.
3. Add the seasoning and cook until it has almost evaporated.
4. Serve with toasted sesame seeds and spring onion.

#### Notes

The size of the lotus-root section and tau kwa, and the stir-frying duration, are not specified.

#### Source

Supplied recipe document.

## Fish and eggs

<a id="japanese-steamed-egg"></a>

### Japanese steamed egg

**ID:** `japanese-steamed-egg`

**Servings:** 5 portions.

**Time:** Steam for 15 minutes.

**Review:** Imported draft.

#### Ingredients

- 4 eggs
- Dashi stock, twice the total egg volume in ml
- Dashi stock packet and 1 tbsp bonito flakes, for the stock; no salt
- 1 tsp soy sauce
- 1 tsp mirin
- 1/2 tofu, described as 1 section in the source
- 1/3 bowl edamame
- 5 crab sticks, each cut into 3 pieces

#### Method

1. Boil the dashi stock packet with the bonito flakes, without salt. Use stock equal to twice the egg volume.
2. Mix the eggs well and strain through a sieve before adding the other ingredients.
3. Cover with cling film and steam for 15 minutes.

#### Notes

- The stock packet size, tofu portion size and bowl size are not specified. The tofu amount is written as "1/2 tofu, one section" in the source.

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
- 3 garlic, minced; unit not specified
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
- The garlic quantity has no unit in the source.

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

**Time:** Steam for 9 minutes.

**Review:** Imported draft.

#### Ingredients

- 250 g fish
- 1/2 packet shimeji mushrooms
- A small knob of ginger, sliced
- 1/2 tbsp soy sauce
- 1 tbsp mirin
- 1 tbsp white miso paste
- 1 tsp butter
- 2 tbsp water

#### Method

1. Mix the ingredients and sauce.
2. Wrap in baking paper and steam for 9 minutes.

#### Notes

- The fish type and mushroom packet size are not specified.

#### Source

Supplied recipe document.

<a id="steamed-pomfret"></a>

### Steamed pomfret

**ID:** `steamed-pomfret`

**Servings:** 5 portions.

**Time:** Steam for 8 minutes; marinating time not specified.

**Review:** Imported draft.

#### Ingredients

- Pomfret; quantity not specified
- 1 tbsp wolfberries
- 1 bottle chicken essence
- Ginger; quantity not specified
- 1 tsp fish soy sauce, optional

#### Method

1. Marinate the pomfret with the wolfberries, chicken essence, ginger and optional fish soy sauce.
2. Steam for 8 minutes and serve.

#### Notes

- The fish weight and chicken essence bottle size are not specified.

#### Source

Supplied recipe document.

<a id="steamed-dory-fillet"></a>

### Steamed dory fillet

**ID:** `steamed-dory-fillet`

**Servings:** 5 portions.

**Time:** Steam for 8 minutes.

**Review:** Imported draft.

#### Ingredients

- 500 g fish, titled as dory
- 2 sprigs spring onion, white parts chopped
- 6 slices ginger
- 2 tbsp minced garlic
- Salt and oil, for sauteing; quantities not specified
- 2 tbsp soy sauce
- 3 tbsp hot water
- 1 tbsp oyster sauce
- 1 tbsp sesame oil
- 1 tsp sugar
- White pepper; quantity not specified

#### Method

1. Pat the fish dry. Place it on the spring onion and ginger and steam for 8 minutes.
2. Saute the garlic in some salt and oil.
3. Prepare a sauce with the soy sauce, hot water, oyster sauce, sesame oil, sugar and white pepper.

#### Notes

- The source does not explain how to combine the garlic, sauce and steamed fish.

#### Source

Supplied recipe document.

<a id="honey-baked-miso-halibut"></a>

### Honey-baked miso halibut

**ID:** `honey-baked-miso-halibut`

**Servings:** 5 portions.

**Time:** Marinate for 2 hours; stand out of the fridge for 15 minutes; bake for 6 minutes and broil for 8 minutes.

**Review:** Imported draft.

#### Ingredients

- 400 g halibut
- 2 tbsp miso
- 1 tbsp mirin
- 1 tbsp maple syrup
- 3/4 tbsp sesame oil
- A sprinkle of black pepper

#### Method

1. Marinate the halibut with the miso, mirin, maple syrup, sesame oil and black pepper for 2 hours.
2. Remove from the fridge 15 minutes before baking.
3. Bake at 180 degrees for 6 minutes.
4. Broil using the oven's top heat for 8 minutes or until slightly charred.

#### Notes

- The source title says honey, but the ingredients specify maple syrup.
- The source gives an oven temperature of 180 degrees without a temperature unit.

#### Source

Supplied recipe document.

<a id="steamed-halibut-garlic-ginger"></a>

### Steamed halibut with garlic and ginger sauce

**ID:** `steamed-halibut-garlic-ginger`

**Servings:** 5 portions.

**Time:** Option 1 not specified. Option 2: steam for 6 minutes.

**Review:** Imported draft.

#### Ingredients

- Option 1: 300 to 500 g halibut, listed as 2 pieces
- Option 1: 1 tsp sesame sauce
- Option 1: 2 slices ginger and 1 tbsp wolfberries, for steaming
- Option 1 sauce: 1 tsp oyster sauce, 1 tsp soy sauce and 1 tsp mirin
- Option 1 aromatics: 2 tbsp ginger sticks, 5 garlic, minced, and 4 sprigs spring onion
- Option 2: 250 g halibut or cod
- Option 2: 2 tbsp shredded ginger, also listed as 1 knob
- Option 2 sauce: 1.5 tsp soy sauce, 1.5 tsp Chinese wine, 1 tsp water and 1 tsp sesame oil
- Option 2: spring onion, for serving; quantity not specified

#### Method

1. For option 1, season the fish with sesame sauce. Steam with 2 slices of ginger and the wolfberries.
2. Stir-fry the ginger sticks and garlic, then add the spring onion. Add the option 1 sauce and cook until thickened. Pour over the steamed fish.
3. For option 2, steam the fish with the shredded ginger for 6 minutes.
4. Fry the option 2 sauce ingredients. Pour over the fish and serve with spring onion.

#### Notes

- Choose one option.
- Option 1 specifies sesame sauce, not sesame oil. The type of sauce is not explained.
- The garlic quantity in option 1 has no unit in the source.

#### Source

Supplied recipe document.

<a id="tomato-egg"></a>

### Tomato egg

**ID:** `tomato-egg`

**Servings:** 5 portions.

**Time:** Fry garlic and onion for about 15 seconds; cook tomatoes for 1 to 2 minutes. Total time not specified.

**Review:** Imported draft.

#### Ingredients

- 5 large eggs, beaten with a sprinkle of salt
- A pinch of salt and white or black pepper
- 3 cloves garlic, minced
- 1 green onion, chopped, with white and green parts kept separate
- 2 medium tomatoes, each cut into 8 wedges
- 2 tbsp ketchup
- 1 tbsp oyster sauce
- 1 tsp wolfberries, soaked and mashed
- 1/3 cup water
- 1 tsp sesame oil
- 2 tbsp oil, divided, for frying

#### Method

1. Heat 1 tbsp oil in a wok over medium-high heat. Add the beaten eggs and stir lightly until just set but still runny. Transfer the eggs back to the bowl and wipe out the pan.
2. Add the remaining 1 tbsp oil. Fry the garlic and white parts of the green onion until fragrant, about 15 seconds.
3. Add the tomatoes, ketchup, oyster sauce, wolfberries and water. Cook for 1 to 2 minutes until the tomatoes soften.
4. Return the eggs to the wok and stir in the sesame oil. Garnish with the green parts of the onion.

#### Notes

- The source does not specify when to add the separate pinch of salt and pepper.

#### Source

- [Cookerru: tomato egg](https://www.cookerru.com/tomato-egg/)

<a id="fried-egg-shallots-spring-onion"></a>

### Fried egg with shallots and spring onion

**ID:** `fried-egg-shallots-spring-onion`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 5 eggs
- 1/2 tsp fish sauce
- 1/2 tsp sesame oil
- 1.5 large shallots
- 2 sprigs spring onion
- 1 tbsp oyster sauce

#### Method

1. Mix the eggs with the fish sauce and sesame oil. Fry and set aside.
2. Fry the shallots and spring onion, then add the oyster sauce.

#### Notes

- The source title says big onion, while the ingredients say large shallots.
- The source does not specify when to return the eggs to the pan.

#### Source

- [Instagram recipe reference](https://www.instagram.com/reel/DDf2XkmyrZi/)

<a id="baked-tomato-fish-foil"></a>

### Baked tomato fish in foil

**ID:** `baked-tomato-fish-foil`

**Servings:** 5 portions.

**Time:** Stir-fry for about 2 minutes; steam vegetables for 6 minutes; bake fish for 15 minutes. Sauce simmering time not specified.

**Review:** Imported draft.

#### Ingredients

- 200 g firm white fish, such as threadfin or cod
- 1.5 tsp olive oil
- 1.5 tsp garlic, chopped
- 1/2 medium onion, chopped
- Italian seasoning; quantity not specified
- 2 tbsp tomato paste
- 2 tomatoes, diced
- 1/2 medium zucchini, cut into matchsticks
- 1/2 medium pumpkin or squash, cut into matchsticks
- 1/2 bell pepper, cut into matchsticks, optional
- A little black pepper
- Salt, if needed

#### Method

1. Stir-fry the onion and garlic for about 2 minutes. Add the Italian seasoning, black pepper, tomato paste and diced tomatoes. Taste and add salt if needed. Simmer until the sauce thickens.
2. Steam the zucchini, pumpkin and optional bell pepper for 6 minutes.
3. Preheat the oven to 180 degrees. Arrange the vegetables evenly on foil, place the fish on top and pour over the sauce. Wrap into a pouch.
4. Bake at 180 degrees for 15 minutes.

#### Notes

- The source gives an oven temperature of 180 degrees without a temperature unit.
- The linked recipe is marked as a reference only.

#### Source

- [Tuttorosso: baked fish in foil packets](https://tuttorossotomatoes.com/recipes/detail/baked-fish-in-foil-packets)

<a id="baked-salmon-teriyaki"></a>

### Baked salmon with teriyaki sauce

**ID:** `baked-salmon-teriyaki`

**Servings:** 5 portions.

**Time:** Marinate for 1 hour; bake for 10 minutes.

**Review:** Imported draft.

#### Ingredients

- 600 g salmon, about 3 pieces
- 1 knob ginger, cut into strips
- 1.5 tsp sesame oil
- 1.5 tbsp sake
- 1.5 tbsp mirin
- 2.5 tbsp soy sauce
- 1 tbsp honey or 1/2 tbsp brown sugar

#### Method

1. Marinate the fish with the sesame oil, sake, mirin, soy sauce and honey or brown sugar for 1 hour.
2. Wrap in baking paper and bake at 180 degrees for 10 minutes.

#### Notes

- The source gives an oven temperature of 180 degrees without a temperature unit.
- The source does not say when to add the ginger.

#### Source

Supplied recipe document.

<a id="ginger-soy-baked-salmon"></a>

### Ginger soy fish with baked salmon

**ID:** `ginger-soy-baked-salmon`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 600 g salmon, about 3 pieces
- 1 knob ginger, cut into strips
- 2 tbsp sesame oil, for frying the ginger
- 1 tbsp reserved ginger oil, to season the salmon
- 1 tbsp soy sauce
- 3 tbsp water
- 1/2 tsp corn starch
- 1 tsp honey

#### Method

1. Fry the ginger strips in the sesame oil. Reserve the oil.
2. Season the salmon with 1 tbsp of the reserved ginger oil.
3. Serve the fish with the sauce and fried ginger strips when ready to eat.

#### Notes

- Keep the sauce separate until serving. The source says the sauce is very thick and salty and should not be doubled.
- The title specifies baked salmon, but the source gives no fish cooking method, temperature or time. It also omits the sauce preparation method.

#### Source

- [Rasa Malaysia: ginger soy fish](https://rasamalaysia.com/ginger-soy-fish/)

<a id="japanese-creamy-fish-stew"></a>

### Japanese creamy fish stew

**ID:** `japanese-creamy-fish-stew`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 5 cloves garlic
- 1 packet brown mushrooms, sliced
- 2.5 tbsp unsalted butter
- 2.5 tbsp plain flour
- 180 ml water or stock
- 1 tbsp dashi or chicken powder, listed as an alternative when stock is unavailable
- 180 ml milk or cream
- 4 baby potatoes
- 2 carrots
- 1 stalk leek
- 1 onion
- 2 to 3 dory, cod or barramundi fillets, 500 to 600 g total, cut into bite-sized pieces

#### Method

1. Boil the potatoes, carrots, onion and leek until soft.
2. In another pan, stir-fry the garlic, then add the mushrooms. Mix in the butter and flour and stir into a roux until no flour remains visible.
3. Stir in 180 ml of the vegetable cooking water or stock. Add the cooked vegetables.
4. Add the milk or cream, bring to a boil and serve. Keep stirring because the cream burns easily.

#### Notes

- The source lists fish but never says when to add or cook it.
- The ingredients specify milk or cream, while the method says milk and cream. Confirm whether these are alternatives.
- The stock-powder alternative is unclear in the source. It reads "180 ml water or stock, if no 1 tbsp dashi/chicken powder".

#### Source

- [Instagram recipe reference](https://www.instagram.com/reel/Cr0IXI5gY-J/)

<a id="sweet-sour-fried-tofu-fish"></a>

### Sweet and sour fried tofu or fish

**ID:** `sweet-sour-fried-tofu-fish`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Option A: 1 box firm tofu
- Option B: 2 tubes egg tofu
- Corn flour, for coating; quantity not specified
- A pinch of mushroom salt and garlic powder
- 1 slice pineapple
- 1 shallot or 1/2 small onion
- 1/2 capsicum
- 1 tbsp pineapple juice
- 2.5 tbsp ketchup
- 1 tbsp soy sauce
- 1/2 tbsp oyster sauce
- 1 tsp sugar or honey
- 1 tbsp apple cider vinegar
- 1.5 tbsp water
- Corn flour slurry; quantity not specified

#### Method

1. Coat the chosen tofu with corn flour, mushroom salt and garlic powder. Stir-fry until crisp and set aside.
2. Stir-fry the onion, capsicum and pineapple until softened.
3. Add the sauce ingredients and cook until thickened.
4. Pour the sauce over the fried tofu before serving.

#### Notes

- The title offers fish, but the source provides no fish quantity or fish method.
- The ingredient list gives 1 slice of pineapple, while the method uses 1/2 slice. Confirm the intended quantity.

#### Source

Supplied recipe document.

## Chicken, pork and beef

<a id="steamed-tofu-egg-pork"></a>

### Steamed tofu and egg with pork

**ID:** `steamed-tofu-egg-pork`

**Servings:** 5 portions.

**Time:** Steam for 8 minutes; marinating time not specified.

**Review:** Imported draft.

#### Ingredients

- 1 box silken tofu
- 2 eggs
- 120 ml chicken broth
- 100 g minced pork
- 1/2 tsp sesame oil, for the pork marinade
- Corn flour, for the pork marinade; quantity not specified
- Sauce: 1 tsp soy sauce, 1 tsp oyster sauce, 1 tbsp water, 1/2 tsp sesame oil and 1/2 tsp sugar

#### Method

1. Marinate the minced pork with the sesame oil and corn flour.
2. Place the tofu in a bowl. Strain the egg over it through a sieve, then add the minced pork.
3. Steam for 8 minutes.
4. Drizzle the sauce over when ready to serve.

#### Notes

- The source does not say when to add the chicken broth or how to prepare the sauce.
- The tofu box size is not specified.

#### Source

- [Instagram recipe reference](https://www.instagram.com/reel/Ce0qJfyNsPl/)

<a id="miso-mapo-tofu"></a>

### Miso mapo tofu

**ID:** `miso-mapo-tofu`

**Servings:** 5 portions.

**Time:** Simmer for 2 minutes; marinating and frying times not specified.

**Review:** Imported draft.

#### Ingredients

- 250 g silken tofu
- 100 g minced chicken
- 1 tsp sesame oil and 1 tsp corn flour, for the meat marinade
- 1 sprig spring onion, chopped
- 1 garlic, minced; unit not specified
- 1/2 tsp minced ginger
- 1 tbsp sake, optional
- 1 tbsp mirin
- 300 ml water
- 1 tbsp miso
- A drizzle of sesame oil
- Corn starch slurry; quantity not specified

#### Method

1. Marinate the minced meat with the sesame oil and corn flour.
2. Fry the ginger and garlic until fragrant, then add the minced meat.
3. Add the tofu and seasoning. Simmer for 2 minutes and thicken with corn starch slurry.
4. Serve with chopped spring onion.

#### Notes

- The ingredients list minced chicken, while the method says pork. Confirm the intended meat.
- The garlic quantity has no unit in the source.

#### Source

Supplied recipe document.

<a id="steamed-chicken-mushrooms-black-fungus"></a>

### Steamed chicken with mushrooms and black fungus

**ID:** `steamed-chicken-mushrooms-black-fungus`

**Servings:** 5 portions.

**Time:** Marinate for at least 30 minutes; steam for 15 minutes or until cooked through.

**Review:** Imported draft.

#### Ingredients

- 3 small chicken thighs, cut into cubes
- 4 red dates, halved
- 1/2 packet black fungus
- 3 dried mushrooms, soaked and thinly sliced
- 1 tbsp wolfberries
- Thinly sliced bak kwa, optional; quantity not specified
- 1 tbsp oyster sauce
- 1 tbsp light soy sauce
- 1 tsp sesame oil
- 1 tsp corn flour
- 1/2 tsp minced ginger
- A dash of white pepper
- Chopped spring onion and coriander, for serving; quantities not specified

#### Method

1. Marinate the chicken with the oyster sauce, light soy sauce, sesame oil, corn flour, ginger and white pepper for at least 30 minutes.
2. Steam the chicken with the other ingredients for 15 minutes or until cooked through.
3. Serve with chopped spring onion and coriander.

#### Notes

- The black fungus packet size is not specified.

#### Source

Supplied recipe document.

<a id="braised-chicken-mushrooms-tau-kwa"></a>

### Braised chicken with mushrooms and tau kwa

**ID:** `braised-chicken-mushrooms-tau-kwa`

**Servings:** 5 portions.

**Time:** Simmer for 30 minutes, then another 10 minutes; soaking and frying times not specified.

**Review:** Imported draft.

#### Ingredients

- 400 g chicken, followed by "2 boneless chicken thighs, 4 drumlets" in the source
- 1/2 cup black fungus
- 2 pieces firm tofu, also called tau kwa
- 8 dried mushrooms; reserve the soaking liquid
- 5 boiled eggs
- 1 knob ginger, sliced
- 2 stalks scallions, halved
- 2 cloves garlic, smashed whole
- 2 bay leaves
- 2 star anise
- 1 cinnamon stick
- 1 tsp cloves
- 1.5 tsp oyster sauce
- 1.5 tsp sesame oil
- 1 tbsp light soy sauce
- 1 tbsp dark soy sauce
- 1 tbsp rock sugar
- 1 tsp fish sauce
- 2 tbsp Shaoxing wine
- 400 ml water or reserved mushroom soaking liquid, or enough to cover the chicken
- Rice or noodles, for serving; quantity not specified

#### Method

1. Soak and slice the mushrooms. Reserve the soaking liquid for the braising sauce.
2. Stir-fry the ginger, garlic, scallions and tau kwa. Remove the tau kwa when lightly browned.
3. Add the chicken and fry lightly. Add 400 ml water or mushroom soaking liquid, the remaining seasoning and aromatics. Simmer for 30 minutes.
4. Add the tau kwa and boiled mushrooms and simmer for another 10 minutes.
5. Serve with rice or noodles.

#### Notes

- The source lists 400 g chicken alongside 2 thighs and 4 drumlets. Confirm the intended amount and whether these cuts are alternatives.
- The source does not say when to add the boiled eggs or black fungus.
- The final step calls for boiled mushrooms, but no mushroom-boiling step is given.

#### Source

Supplied recipe document.

<a id="soya-chicken-potato-stew"></a>

### Soya chicken and potato stew

**ID:** `soya-chicken-potato-stew`

**Servings:** 5 portions.

**Time:** Simmer for 30 minutes; add optional sweet potato for the final 10 to 15 minutes.

**Review:** Imported draft.

#### Ingredients

- 2 small potatoes
- 1 small sweet potato, optional
- 2 carrots
- 800 g chicken, chopped into bite-sized pieces
- 5 cloves garlic
- Cooking oil; quantity not specified
- 1 tbsp light soy sauce
- 400 ml water
- 1 tbsp dark soy sauce
- 1 tbsp wolfberries
- 1 tsp rock sugar, optional, to balance the taste
- 1 tbsp sesame oil

#### Method

1. Heat cooking oil in a wok and saute the garlic until golden brown.
2. Add the chicken and stir-fry until the meat turns white.
3. Add the carrots and potatoes and stir-fry to combine. Add the light soy sauce and mix well.
4. Add the water, dark soy sauce and wolfberries. Stir briefly, cover and simmer for 30 minutes.
5. If using sweet potato, add it only for the final 10 to 15 minutes so it does not turn mushy.
6. Add the sesame oil and stir to combine.

#### Notes

- The source says to omit the sugar when using sweet potato. It does not specify when to add the optional sugar.

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
2. Preheat the oven to 190 degrees.
3. Wrap and seal the chicken in cooking paper or foil. Bake for 35 minutes.
4. Open the paper or foil, glaze with honey and bake for another 5 to 10 minutes to brown the chicken.

#### Notes

- The source gives an oven temperature of 190 degrees without a temperature unit.

#### Source

Supplied recipe document.

<a id="potatoes-carrots-minced-meat"></a>

### Potatoes and carrots with minced meat

**ID:** `potatoes-carrots-minced-meat`

**Servings:** 5 portions.

**Time:** Simmer for 10 minutes; marinating and frying times not specified.

**Review:** Imported draft.

#### Ingredients

- 5 cloves garlic, minced
- 1 sprig spring onion
- 200 g minced chicken or pork
- 1.5 tsp corn flour and 1 tsp soy sauce, for the meat marinade
- 2 carrots, cubed
- 5 baby potatoes, cubed
- 1.5 onions, cubed
- 1 tbsp oyster sauce
- 1 tbsp dark soy sauce
- 1 tsp soy sauce, for the seasoning
- Water, enough to cover the ingredients
- Corn flour mixed with water, for thickening; quantities not specified

#### Method

1. Marinate the minced meat with 1.5 tsp corn flour and 1 tsp soy sauce.
2. Stir-fry the garlic, spring onion, onion and minced meat until fragrant. Add the carrots and potatoes and fry until soft.
3. Add enough water to cover the ingredients. Simmer for 10 minutes and check that the carrots and potatoes are soft.
4. Add the seasoning and mix well. Stir in corn flour mixed with water to thicken the sauce.

#### Notes

- The source also calls this dish "ABC".

#### Source

- [YouTube recipe reference](https://youtu.be/ZZXg7FYuiLI)

<a id="beef-pork-tomato-stew"></a>

### Beef or pork tomato stew

**ID:** `beef-pork-tomato-stew`

**Servings:** 5 portions.

**Time:** Simmer for 1.5 hours, then leave the pot closed for 1 hour.

**Review:** Imported draft.

#### Ingredients

- 1 onion
- 1.5 carrots
- 4 potatoes
- 500 to 700 g beef chuck, beef brisket or pork collar
- 500 ml water
- 1 sprig basil
- 1 tsp Italian herbs
- 2 tomatoes, skins removed and cubed
- 1 tbsp butter
- 1 bottle pasta sauce
- 1 packet dried raisins

#### Method

1. Cut the ingredients into large cubes and the onion into large slices.
2. Fry the beef or pork cubes with the butter until lightly browned.
3. Add the onion, tomatoes, potatoes and carrots. Fry lightly and mix well.
4. Add the pasta sauce, water and raisins.
5. Simmer for 1.5 hours using a vacuum pot, then leave the pot closed for another 1 hour.

#### Notes

- The ingredients list 500 ml water, while the method says 1 bottle of water. The bottle size is not specified.
- The pasta sauce bottle and raisin packet sizes are not specified.
- The source does not say when to add the basil and Italian herbs.

#### Source

Supplied recipe document.

<a id="minced-beef-tacos"></a>

### Minced beef for tacos

**ID:** `minced-beef-tacos`

**Servings:** 5 portions.

**Time:** Bake with cheese for about 8 minutes; frying time not specified.

**Review:** Imported draft.

#### Ingredients

- 400 g fresh minced beef
- 1 onion, cut into small cubes
- 2 cloves garlic, minced
- 2 tbsp tomato paste
- 50 ml water
- A sprinkle of black pepper
- 1 tsp all-purpose seasoning, or 1 tsp paprika plus 1 tsp mushroom salt
- 1 tsp oregano or Italian herbs
- 1 tsp garlic powder
- 1 tsp onion powder
- 1 tbsp oil
- Cheese; quantity not specified

#### Method

1. Stir-fry the onion and garlic in the oil until slightly softened.
2. Add the beef and fry until it turns light brown.
3. Add the seasoning and mix until the beef is cooked.
4. Add the tomato paste and water. Cook until the water evaporates and the filling is juicy rather than watery.
5. Bake with cheese for about 8 minutes until melted.

#### Notes

- The baking temperature and cheese quantity are not specified. The source does not describe taco assembly.

#### Source

- [RecipeTin Eats: ground beef tacos](https://www.recipetineats.com/ground-beef-tacos-recipe/#recipe)

<a id="japanese-pork-stew"></a>

### Japanese pork stew

**ID:** `japanese-pork-stew`

**Servings:** 5 portions.

**Time:** Simmer vegetables for 30 minutes; pork cooking time not specified.

**Review:** Imported draft.

#### Ingredients

- 2 carrots
- 1 radish
- 1 brown onion, chopped into small pieces
- 1,000 ml water
- 1 dashi packet
- 2 tbsp miso
- 200 g pork shabu
- 1 tsp minced ginger
- 1 tsp sesame oil

#### Method

1. Stir-fry the ginger and onion with the sesame oil.
2. Add the carrots and radish and fry lightly.
3. Add the dashi packet and water. Simmer for 30 minutes.
4. When the vegetables are soft, add the miso paste and meat.

#### Notes

- The ingredient list calls for chopped onion, while the method says sliced onion.
- The source ends when the meat is added and gives no further cooking time or doneness instruction.

#### Source

- [Instagram recipe reference](https://www.instagram.com/reel/C7L1ZVTSoRE/)

<a id="garlicky-stir-fried-beef"></a>

### Garlicky stir-fried beef

**ID:** `garlicky-stir-fried-beef`

**Servings:** 5 portions.

**Time:** Marinate for 3 hours or longer; fry beef for 2 minutes per side; cook bean sprouts for 3 minutes.

**Review:** Imported draft.

#### Ingredients

- 200 g skirt beef
- 2 sprigs spring onion
- 4 cloves garlic
- 1 packet bean sprouts
- 1/2 thumb-sized piece of ginger, shredded
- 1 tsp soy sauce
- 1.5 tsp sesame oil
- 1 tbsp corn flour
- 1/4 tsp baking soda
- 1 tbsp water
- Additional seasoning, mentioned in the method but not specified

#### Method

1. Marinate the beef with the soy sauce, sesame oil, corn flour, baking soda and water for 3 hours or longer.
2. Remove from the fridge and bring to room temperature before cooking, as stated in the source.
3. Pan-fry the beef for 2 minutes on each side, then set aside.
4. Fry the garlic, ginger and spring onion until fragrant. Add the bean sprouts and cook for 3 minutes until slightly soft.
5. Add the seasoning and beef. Mix well before serving.

#### Notes

- The final step refers to seasoning that is not defined separately in the source.
- The bean sprout packet size is not specified. The source does not give a duration for bringing the beef to room temperature.

#### Source

- [I Heart Umami: beef with garlic sauce](https://iheartumami.com/beef-with-garlic-sauce/)

<a id="sweet-sour-pork-ribs"></a>

### Sweet and sour pork ribs

**ID:** `sweet-sour-pork-ribs`

**Servings:** 5 portions.

**Time:** Blanch for 5 minutes; simmer for 1 hour; final sauce reduction time not specified.

**Review:** Imported draft.

#### Ingredients

- 700 g pork ribs
- 1 sprig spring onion and 3 slices ginger, for blanching
- Water, for blanching; quantity not specified
- 2 to 3 tbsp oil
- 3 tbsp rock sugar
- 500 ml hot water, for the sauce
- 2 sprigs spring onion and 5 slices ginger, for the sauce
- 1.5 tbsp Dog brand black vinegar
- 2 tbsp oyster sauce
- 2 tbsp soy sauce

#### Method

1. Blanch the pork ribs in boiling water with 1 sprig spring onion and 3 slices ginger for 5 minutes. Rinse to remove the blood foam.
2. Heat the oil in a pan. Add the rock sugar and stir until melted without burning it.
3. Add the pork ribs and fry until brown and sticky.
4. Add the hot water, remaining spring onion and ginger, vinegar, oyster sauce and soy sauce. Simmer for 1 hour.
5. Open the lid to thicken the sauce. Taste and adjust the seasoning if needed.

#### Source

- [Kitchen Misadventures: sweet and sour pork ribs](https://kitchenmisadventures.com/sweet-and-sour-pork-rib)

## Mains (rice and noodles)

<a id="fried-brown-rice-chicken"></a>

### Fried brown rice with chicken

**ID:** `fried-brown-rice-chicken`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- Corn, quantity not specified
- Carrot, quantity not specified
- Cabbage, quantity not specified
- Garlic: 6, unit not specified
- Eggs: 3 in the ingredient list, but 2 in the egg seasoning instructions
- Rice, quantity not specified
- 1 tbsp soy sauce, for seasoning
- 1 tbsp dark soy sauce
- 1/4 tsp red sugar
- 1 tbsp chicken powder, no salt
- 1 tbsp sesame oil, for frying the rice
- 1 tsp Chinese wine, for seasoning the eggs
- 1/2 tsp fish sauce, for seasoning the eggs
- 150 g chicken fillet
- Corn flour, quantity not specified, for marinating the chicken
- 1 tsp soy sauce, for marinating the chicken

#### Method

1. Season the eggs with the Chinese wine and fish sauce. The source gives conflicting egg quantities; see Notes.
2. Season the chicken with corn flour and 1 tsp soy sauce.
3. Stir-fry the ingredients and rice separately. Use the sesame oil for the rice. Mix everything together when ready.

#### Notes

- The ingredient list says 3 eggs; the egg seasoning section says 2 eggs. Confirm the intended quantity.
- The source lists the rice seasoning but does not state when to add it.

#### Source

Supplied recipe document.

<a id="fried-basmati-rice-chicken-seafood"></a>

### Fried basmati rice with chicken and seafood

**ID:** `fried-basmati-rice-chicken-seafood`

**Servings:** 5 portions.

**Time:** Prawn soak: 30 minutes. Other times not specified.

**Review:** Imported draft.

#### Ingredients

- 1/3 packet crab sticks
- 12 prawns
- 1 carrot, cubed
- 1 cup prepared corn
- 1 slice barbecue pork, shredded
- 2 heads garlic, minced
- 1 large shallot, sliced
- 4 eggs
- 1 cup basmati rice, marinated with 1 tsp sesame oil
- 50 g minced chicken
- 2 sprigs spring onion
- Fried shallots, quantity not specified
- 1 tsp baking soda, for soaking the prawns
- 1 tsp sugar, for soaking the prawns
- Ice water, quantity not specified, for soaking the prawns
- 1 tsp light soy sauce, for marinating the prawns
- 1/2 tsp sesame oil, for marinating the prawns
- Cornstarch, a sprinkle, for marinating the prawns
- 1 tsp chicken bouillon mixed with 1 tsp water
- Black pepper, a sprinkle

#### Method

1. Shell and devein the prawns. Soak them with 1 tsp baking soda, 1 tsp sugar, and ice water for 30 minutes, then rinse. Marinate with 1 tsp light soy sauce, 1/2 tsp sesame oil, and a sprinkle of cornstarch.
2. Fry the eggs, prawns, and crab sticks separately and set aside. Scramble the eggs, and fry the prawns with 1 tsp of the garlic.
3. Fry shallot and garlic. Add the carrot and corn, fry until soft, and set aside.
4. Fry shallot and garlic again. Add the minced chicken and barbecue pork and fry until fragrant. Add the rice, then stir in the chicken bouillon mixed with water.
5. Return the corn, carrot, prawns, and crab sticks to the pan. Fry until dry and a little browned for wok hei, then add black pepper, spring onion, and the scrambled eggs.

#### Notes

- The original title names chicken; the recipe also includes prawns, crab sticks, and barbecue pork.
- The source does not specify whether the 1 cup of rice is measured before or after cooking, or how the rice is prepared before frying.
- The listed fried shallots have no stated serving step. The source does not allocate all garlic and shallot between the separate frying steps.

#### Source

Supplied recipe document.

<a id="fried-brown-rice-reduced-seasoning"></a>

### Fried brown rice, reduced seasoning

**ID:** `fried-brown-rice-reduced-seasoning`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 1 sprig spring onion, chopped
- 50 g corn
- 1/2 carrot
- 50 g cabbage
- Garlic: 8, minced; unit not specified
- 1 knob ginger, minced
- 3 eggs
- 1 cup rice
- 1 tbsp soy sauce, for seasoning
- 1 tbsp dark soy sauce
- 1/4 tsp red sugar
- 1 tbsp chicken powder, no salt
- 1/2 tsp Chinese wine, for seasoning the eggs
- 1/4 tsp fish sauce, for seasoning the eggs
- 150 g chicken fillet
- Corn flour, quantity not specified, for marinating the chicken
- Mushroom salt, a pinch, for marinating the chicken
- 3 tbsp oil

#### Method

1. Season the eggs with the Chinese wine and fish sauce. Season the chicken with corn flour and a pinch of mushroom salt.
2. Stir-fry the garlic and ginger in 3 tbsp oil until brown. Use the same oil to stir-fry the chicken, then add the white part of the spring onion. Reserve the oil for the rice.
3. Stir-fry the eggs and vegetables separately.
4. Combine all the ingredients and rice, then add the seasoning.

#### Notes

- The source calls this a reduced-seasoning version suitable when serving other dishes.
- The original title allows chicken or pork, but the ingredient list specifies 150 g chicken fillet and gives no separate pork instructions.
- The source does not specify whether the rice is measured before or after cooking, or how to prepare it before frying.

#### Source

Supplied recipe document.

<a id="miso-butter-corn-fried-rice-chicken"></a>

### Miso butter corn fried rice with chicken

**ID:** `miso-butter-corn-fried-rice-chicken`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 3/4 tbsp miso paste mixed with 1 tbsp water
- Canned corn, drained, quantity not specified; reserve its liquid
- 1 cup overnight rice; brown rice is suitable
- 1/2 zucchini, cubed
- 1 carrot, cubed
- 150 g chicken, sliced
- Corn flour, quantity not specified, for marinating the chicken
- 1/2 tsp soy sauce, for marinating the chicken
- 3 garlic cloves, minced
- Olive oil, a little
- 1 tbsp butter
- 2 tbsp reserved corn liquid

#### Method

1. Marinate the chicken with corn flour and 1/2 tsp soy sauce.
2. Use a little olive oil to fry the garlic and vegetables, then set aside. Fry the marinated chicken and set aside.
3. Fry the drained corn with 1 tbsp butter and 2 tbsp corn liquid. Add the rice and stir-fry until it is not too wet, then add the vegetables and chicken.

#### Notes

- The source lists the miso mixture as seasoning but does not state when to add it.

#### Source

Supplied recipe document.

<a id="soya-mee-soup"></a>

### Soya mee soup

**ID:** `soya-mee-soup`

**Servings:** 5 portions.

**Time:** Soup: boil for 1 hour. Other times not specified.

**Review:** Imported draft.

#### Ingredients

- 150 g minced pork or chicken
- 1 tbsp minced garlic
- 10 g black fungus, shredded
- 1/2 cup dried anchovies, rinsed twice
- 10 prawns, or chicken bones of an unspecified quantity
- 1/2 cup yellow beans
- 1 sweet date
- 2 bundles soya mee
- 4 boiled eggs
- 1 bunch leafy vegetables
- 6 small shallots, fried, for an optional topping
- 2 slices ginger
- 1/2 tbsp light soy sauce, for marinating the meat
- 1 tbsp sesame oil, for marinating the meat
- 1 tsp cornstarch, for marinating the meat
- 1 tbsp oyster sauce
- 100 ml water, for the meat mixture
- Water for the soup, quantity not specified
- Fried anchovies, optional topping, quantity not specified

#### Method

1. Boil the prawn shells and legs, or chicken bones, with the ginger, sweet date, dried anchovies, and yellow beans for 1 hour.
2. Marinate the minced meat with the light soy sauce, sesame oil, and cornstarch.
3. Fry the garlic. Add the marinated meat and stir-fry, then add the shredded black fungus. Mix in the oyster sauce and 100 ml water.
4. Serve with the soya mee, boiled eggs, and leafy vegetables. Top with fried anchovies and fried shallots if desired.

#### Notes

- The soup water quantity, noodle cooking method, and leafy vegetable preparation are not specified.
- For the prawn version, the source describes using the shells and legs for stock but does not explain how to cook or serve the prawn meat.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.instagram.com/reel/C4sYVukySZ1/)

<a id="vietnamese-beef-noodle-soup"></a>

### Vietnamese beef noodle soup

**ID:** `vietnamese-beef-noodle-soup`

**Servings:** 5 portions.

**Time:** Vacuum pot: 2 hours.

**Review:** Imported draft.

#### Ingredients

- 500 g oxtail
- 400 g beef brisket
- 1 radish
- 1 carrot
- 1 onion
- 2 sprigs spring onion
- 4 slices ginger
- 3 star anise
- 5 cloves
- 3 bay leaves
- 1.5 litres water
- 1 tbsp oyster sauce
- 2 tbsp soy sauce
- Spinach, for serving, quantity not specified
- Mung bean noodles, for serving, quantity not specified
- Coriander, for serving, quantity not specified

#### Method

1. Boil in a vacuum pot for 2 hours.
2. Serve with spinach, mung bean noodles, and coriander.

#### Notes

- The source does not describe ingredient preparation, the timing for adding the seasoning, or how to cook the noodles and spinach.

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

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 2 tbsp sukiyaki sauce
- 1.5 tbsp mirin
- 1 tbsp sake
- 160 ml water
- 1/2 tsp brown sugar, optional
- 2 chicken thighs
- 1 large yellow onion
- Spring onion, quantity not specified
- 2 eggs
- Rice, for serving, quantity not specified

#### Method

1. Fry the onion and chicken until tender and the chicken is no longer pink, then set aside.
2. When ready to eat, crack 2 eggs. Lightly break the yolks and cut through the whites so they remain distinct with a marble pattern.
3. Add two-thirds of the eggs, ideally with more whites, to the centre of the simmering chicken mixture. Avoid the edges of the pan.
4. Add the remaining one-third, ideally with more yolks, across the whole surface of the pan.
5. Serve with rice.

#### Notes

- The source gives 2 eggs in the method.
- The source does not state when to combine the sauce ingredients, how to bring the chicken mixture to a simmer after setting it aside, or when to add the spring onion. Confirm these gaps before relying on this draft.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.justonecookbook.com/oyakodon/)

<a id="ginger-scallion-chicken-rice-noodles"></a>

### Ginger scallion chicken rice noodles

**ID:** `ginger-scallion-chicken-rice-noodles`

**Servings:** 5 portions.

**Time:** Mushrooms and black fungus: stir-fry for 1 minute. Other times not specified.

**Review:** Imported draft.

#### Ingredients

- Thick vermicelli noodles, also called laksa noodles: source quantity is "1 pts"; unit not specified
- 1 packet leafy vegetables, such as nai bai
- 8 slices ginger
- 2 spring onions
- 4 large mushrooms, sliced
- 10 g black fungus
- 600 g chicken
- 1 tbsp corn flour, for marinating the chicken
- 1.5 tbsp soy sauce, for marinating the chicken
- 2 tbsp dark soy sauce, for marinating the chicken
- 2 tbsp Chinese wine, for marinating the chicken
- 1 tbsp sesame oil, for marinating the chicken
- 200 ml water

#### Method

1. Marinate the chicken with the corn flour, soy sauce, dark soy sauce, Chinese wine, and sesame oil.
2. Stir-fry the ginger and spring onions until fragrant. Add the mushrooms and black fungus and stir-fry for 1 minute.
3. Add the marinated chicken. Pour in 200 ml water and bring to a boil, then add the vermicelli and vegetables.

#### Notes

- The source abbreviates the noodle quantity as "1 pts". Confirm the intended unit and amount.
- The source does not specify noodle preparation, black fungus soaking, or the final cooking time after adding the noodles and vegetables.

#### Source

Supplied recipe document.

<a id="soy-milk-ramen"></a>

### Soy milk ramen

**ID:** `soy-milk-ramen`

**Servings:** 5 portions.

**Time:** Soak: 30 minutes to 1 hour. Soup: simmer for 1 hour. Eggs: boil for 8 minutes.

**Review:** Imported draft.

#### Ingredients

- 1 large kombu sheet, described as 4 inches
- 12 small dried mushrooms
- 1.5 litres water
- 2 tbsp minced garlic, plus an unspecified amount for frying the chicken
- 3 tsp minced ginger, plus an unspecified amount for frying the chicken
- 1 onion, chopped
- 2 tbsp sesame oil
- 1 corn cob, for the soup base
- 1 carrot
- 1 sweet date
- Soup pack, type and quantity not specified; add only after tasting
- 2.5 tbsp miso
- 300 ml unsweetened soy milk
- 2.5 packets ramen noodles
- 1 bowl corn, for serving
- Nai bai, quantity not specified
- 1/2 packet shimeji mushrooms
- 1 packet silken tofu
- Chicken, quantity not specified
- 1 tsp soy sauce, for marinating the chicken
- 1/2 tsp "sesame", as written in the chicken marinade; form unclear
- Corn flour, quantity not specified, for marinating the chicken
- 5 eggs

#### Method

1. Lightly rinse the white dust from the kombu. Soak it with the dried mushrooms in 1.5 litres water for 30 minutes to 1 hour.
2. Stir-fry the minced garlic, minced ginger, and onion with 2 tbsp sesame oil until fragrant.
3. Combine the fried aromatics with the soaked ingredients and soaking water. Add the corn cob, carrot, and sweet date and simmer for 1 hour. Remove the kombu when the water boils; the source notes it may otherwise make the broth slimy.
4. Taste before adding any soup pack and the 2.5 tbsp miso.
5. Turn off the heat, then add 300 ml unsweetened soy milk.
6. Marinate the chicken with soy sauce, the stated "sesame", and corn flour. Stir-fry it with some garlic and ginger.
7. Boil the eggs for 8 minutes.

#### Notes

- The chicken marinade says "sesame" without specifying oil, seeds, or another form. Confirm before using it.
- The source lists the ramen, serving corn, nai bai, shimeji mushrooms, and tofu but does not specify their preparation or the final assembly.
- The soup pack type and quantity, chicken quantity, and packet sizes are not specified.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.instagram.com/reel/C9ujt4ISo-T/)

<a id="stir-fried-beehoon-fish-chicken"></a>

### Stir-fried beehoon with fish or chicken

**ID:** `stir-fried-beehoon-fish-chicken`

**Servings:** 5 portions.

**Time:** Beehoon soak: 6 to 8 minutes. Other times not specified.

**Review:** Imported draft.

#### Ingredients

- 1/2 packet brown rice beehoon, Chilli brand
- Garlic: 5, unit not specified
- 1 large shallot
- 1 tbsp dried shrimp, soaked and smashed
- Cabbage, shredded, quantity not specified
- Carrot, grated, quantity not specified
- 3 bean sticks, soaked and sliced, optional
- 1 packet bean sprouts
- 4 eggs
- 1/2 tsp fish sauce, for seasoning the eggs
- 1/2 tsp sesame oil, for seasoning the eggs
- 200 g sliced fish or 2 chicken thighs, cubed
- 1 tsp corn flour, for marinating the fish or chicken
- 1 tsp soy sauce, for marinating the fish or chicken
- 1 tbsp oyster sauce, for the beehoon seasoning
- 1 tbsp soy sauce, for the beehoon seasoning
- 1 tbsp black soy sauce, for the beehoon seasoning
- 1/2 tsp sugar
- 250 ml water
- 1/2 tsp chicken bouillon
- 3 tbsp oil
- Snow peas, corn, fish cake, and mushrooms, optional; quantities not specified

#### Method

1. Soak the beehoon for 6 to 8 minutes. Season the eggs with fish sauce and sesame oil. Marinate the fish or chicken with corn flour and soy sauce.
2. Fry the fish or chicken and set aside. Fry the eggs and set aside.
3. Heat 3 tbsp oil and fry the garlic, shallot, and soaked, smashed dried shrimp until fragrant. Add the bean sticks if using.
4. Add the other vegetables and optional ingredients, then mix in the beehoon and its seasoning.
5. Serve with the eggs and fish or chicken when ready.

#### Notes

- The source gives no final cooking duration or individual preparation details for the optional ingredients.

#### Source

Supplied recipe document.

<a id="tomato-curry-udon"></a>

### Tomato curry udon

**ID:** `tomato-curry-udon`

**Servings:** 5 portions.

**Time:** Simmer: 15 minutes, or until onions and tomatoes are soft.

**Review:** Imported draft.

#### Ingredients

- 4 tomatoes, peeled and diced
- 2 onions, diced
- 3 curry cubes
- Curry powder, additional if required; quantity not specified
- 1 apple or 1 packet raisins
- 1.2 litres dashi stock
- Minced pork or chicken, quantity not specified
- 1 tsp corn flour, for marinating the meat
- Soy sauce, for marinating the meat; quantity not specified
- Tofu, quantity not specified
- Noodles, for serving; quantity and exact type not specified in the ingredient list
- Leafy vegetables, for serving; quantity not specified

#### Method

1. Marinate the minced pork or chicken with corn flour and soy sauce.
2. Fry the meat and diced onions until fragrant. Add the peeled, diced tomatoes and fry until paste-like.
3. Pour in the dashi stock and mix in the curry cubes. Add the apple or raisins.
4. Simmer for 15 minutes, or until the onions and tomatoes are soft.
5. Serve with noodles, tofu, and leafy vegetables.

#### Notes

- The title specifies udon, while the serving instruction says noodles. The source does not provide noodle quantities or cooking instructions, tofu or vegetable preparation, or the meat quantity.
- The source allows more curry powder if required but does not specify its amount or when to add it.
- Tracking parameters and an embedded access token were removed from the original recipe link.

#### Source

Supplied recipe document.

- [Original recipe link](https://daigasikfaan.co/15-minute-tomato-beef-curry-udon/)

<a id="seafood-white-beehoon"></a>

### Seafood white beehoon

**ID:** `seafood-white-beehoon`

**Servings:** 5 portions.

**Time:** Broth: 30 minutes; clams during the final 15 minutes. Prawn soak: 30 minutes. Beehoon soak: 3 minutes. Initial prawn and fish fry: 1 to 2 minutes.

**Review:** Imported draft.

#### Ingredients

- 6 garlic cloves
- 1 sprig spring onion
- 2 large slices ginger
- 15 prawns; reserve the shells and legs for stock
- Clams, 2 scoops as purchased from Sheng Siong; scoop size not specified
- 200 to 300 g fish
- 1 tsp cornstarch, for marinating the fish
- 1 tsp sesame oil, for marinating the fish
- 4 eggs
- 100 g pork collar, sliced
- 1 bunch leafy vegetables
- 1/2 cup yellow beans
- 4 bundles yam beehoon
- 2 packets low-sodium chicken stock; packet volume unclear
- 1/2 tsp ground white pepper
- 1/2 to 1 tbsp fish sauce, depending on the saltiness of the chicken stock
- 1 to 1.5 tbsp cooking wine
- 1 tsp baking soda, for soaking the prawns
- 1 tsp sugar, for soaking the prawns
- Cold water, enough to cover the prawns
- 1 tsp sesame oil, for marinating the prawns
- 1 tsp soy sauce, for marinating the prawns
- Cornstarch, for marinating the prawns; quantity not specified

#### Method

1. Fry the prawn shells and legs with the ginger and spring onion. Add the yellow beans and chicken stock and simmer for 30 minutes. The source's instruction for the stock volume is unclear; see Notes.
2. Remove the prawn shells. The source says to add the clams for the final 15 minutes of the broth cooking and bring to a boil. Set the clams aside for serving.
3. Rub the shelled prawns with 1 tsp baking soda and 1 tsp sugar. Soak in enough cold water to cover for 30 minutes, then rinse. Marinate with 1 tsp sesame oil, 1 tsp soy sauce, and cornstarch.
4. Marinate the fish with 1 tsp cornstarch and 1 tsp sesame oil.
5. Soak the beehoon in hot water for 3 minutes and set aside when softened.
6. Fry garlic with the prawns and fish for 1 to 2 minutes, until half cooked, and set aside. Scramble the eggs until half cooked and set aside.
7. Fry garlic with the pork. Add the broth seasoning and broth and bring to a boil. Add the beehoon and the remaining ingredients before serving.

#### Notes

- The source specifies 4 bundles beehoon and 2 stock packets. It describes the stock as "2 pkt chicken broth (2ltr pkt)". Confirm whether 2 litres is the total volume or each packet's volume.
- The ingredient list allows 200 to 300 g fish, while the frying instruction says 200 g.
- The clam instruction appears twice in the source; it is retained once here. Its order relative to the 30-minute simmer and shell removal is unclear.
- The source does not specify the final cooking time after the partly cooked prawns, fish, and eggs return to the pan.

#### Source

Supplied recipe document.

- [Original recipe link](https://whattocooktoday.com/singapore-seafood-white-bee-hoon.html)

<a id="white-braised-hokkien-mee"></a>

### White braised Hokkien mee

**ID:** `white-braised-hokkien-mee`

**Servings:** 5 portions.

**Time:** Broth: 30 minutes; clams during the final 15 minutes. Prawn soak: 30 minutes. Initial prawn and optional fish fry: 1 to 2 minutes.

**Review:** Imported draft.

#### Ingredients

- 6 garlic cloves
- 1 sprig spring onion
- 2 large slices ginger
- 1/2 onion, sliced
- 8 prawns; reserve the shells and legs for stock
- Clams, 1 scoop; scoop size not specified
- 200 g fish, optional
- 1 tsp cornstarch and 1 tsp sesame oil, for marinating the optional fish
- 2 eggs, with a slurry of 1 tbsp cornstarch and 3 tbsp water
- 100 g pork collar, sliced
- 1 tsp corn flour, 1 tsp sesame oil, a little salt, and white pepper, for marinating the pork collar
- 50 g pork belly, optional, for rendering oil
- 1 bunch leafy vegetables
- 4 packets yellow noodles
- 1/2 packet seafood tofu, sliced
- 1 bundle Chinese spinach
- 1 packet chicken broth, 1 litre
- 1 tbsp cooking wine
- 1/2 tsp ground white pepper, for the broth
- 1 tsp baking soda and 1 tsp sugar, for soaking the prawns
- Cold water, enough to cover the prawns
- 1 tsp cornstarch and 1/2 tsp soy sauce, for marinating the prawns
- Salt or Better Than Bouillon chicken stock, if needed; quantity not specified

#### Method

1. Fry the prawn shells and legs with the ginger and spring onion. Add 1 litre chicken broth and simmer for 30 minutes. Remove the shells. The source says to add cooking wine, ground white pepper, and clams during the final 15 minutes and bring to a boil. Set the clams aside for serving.
2. Rub the shelled prawns with baking soda and sugar and soak in cold water for 30 minutes, then rinse. Marinate with 1 tsp cornstarch and 1/2 tsp soy sauce.
3. Marinate the pork collar and optional fish with their listed seasonings.
4. Fry garlic with the prawns and optional fish for 1 to 2 minutes, until half cooked, then set aside.
5. Fry garlic with the pork belly and/or pork collar. Add the broth and tofu. Bring to a boil, then add the egg slurry. Taste and add salt or Better Than Bouillon chicken stock if needed.
6. Prepare and boil the Chinese spinach separately to remove the iron taste noted in the source.
7. When ready to serve, bring the broth mixture to a boil and add the noodles and remaining ingredients.

#### Notes

- The source lists 4 packets of yellow noodles; packet size is not specified.
- The sliced onion and separate bunch of leafy vegetables are listed without specific cooking steps.
- The egg ingredient lists 2 eggs with cornstarch and water; the method calls this an egg slurry without explaining how to combine it.
- The order of shell removal and adding clams during the final 15 minutes is unclear. The final cooking time after returning the partly cooked prawns and fish is not specified.

#### Source

Supplied recipe document.

<a id="dashi-garlic-butter-fried-rice"></a>

### Dashi garlic butter fried rice

**ID:** `dashi-garlic-butter-fried-rice`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 1 tbsp olive oil
- 2 tbsp unsalted butter
- 10 garlic cloves, pressed
- 2 rice-cooker cups uncooked Japanese rice
- 1/2 tbsp dashi powder
- 1/2 tbsp light soy sauce
- 150 g chicken, sliced
- Corn flour, for marinating the chicken; quantity not specified
- 1/2 tsp soy sauce, for marinating the chicken
- Vegetables, mentioned in the method; types and quantities not specified

#### Method

1. Cook the Japanese rice; add it to the pan while warm.
2. Marinate the chicken with corn flour and 1/2 tsp soy sauce.
3. Use a little olive oil to fry the garlic and vegetables, then set aside. Fry the marinated chicken and set aside.
4. Fry the rice and seasoning until well mixed, then add the other ingredients.

#### Notes

- The original title allows chicken or pork, but the ingredient list specifies chicken and gives no separate pork instructions.
- The source does not specify the vegetables or when to add the listed butter. Rice-cooker cup volume is not stated.

#### Source

Supplied recipe document.

<a id="pumpkin-rice"></a>

### Pumpkin rice

**ID:** `pumpkin-rice`

**Servings:** 5 portions.

**Time:** Chicken marinade: at least 30 minutes. Cooking time not specified.

**Review:** Imported draft.

#### Ingredients

- 1.5 cups rice
- Water and stock: source says "2 cups water (1 cup chicken stock)"; total quantity unclear
- 300 g pumpkin, cut into large cubes
- 6 dried mushrooms, soaked and sliced; reserve the soaking water
- 200 g minced chicken
- 1 tsp soy sauce and 1 tsp sesame oil, for marinating the chicken
- 3 large shallots
- Garlic: 4, minced; unit not specified
- 6 to 8 small scallops, soaked, smashed, and roughly chopped; fresh or dried form not specified
- 1 tbsp oyster sauce, for seasoning
- 1 tbsp soy sauce, for seasoning

#### Method

1. Marinate the minced chicken with 1 tsp soy sauce and 1 tsp sesame oil for at least 30 minutes.
2. Fry the shallots, garlic, scallops, and mushrooms. Add the meat and pumpkin, then add the rice and seasoning and mix well.
3. Cook as usual in a rice cooker. The source suggests trying water-to-rice ratios of 0.8:1 for white rice and 1.3:1 for basmati or brown rice.

#### Notes

- The original title allows chicken or pork, but the ingredient list specifies minced chicken and gives no separate pork instructions.
- Confirm whether the 1 cup chicken stock is included in the 2 cups water or additional. The stated liquid amounts also need reconciliation with the suggested water-to-rice ratios.
- The source asks to reserve the mushroom soaking water but does not say how much to use or whether it replaces another liquid.

#### Source

Supplied recipe document.

- [Original recipe link](https://thedomesticgoddesswannabe.com/2015/07/pumpkin-rice-with-pork-belly-chinese-sausage-and-dried-scallops/)

<a id="tomato-pasta-sauce-bottled"></a>

### Tomato pasta sauce using bottled sauce

**ID:** `tomato-pasta-sauce-bottled`

**Servings:** 5 portions.

**Time:** Yoghurt, milk, and optional cheese: final 2 minutes. Other times not specified.

**Review:** Imported draft.

#### Ingredients

- 1 bottle pasta sauce
- 1 large tomato, diced
- 1 onion, diced
- Garlic: 4, minced; unit not specified
- 50 g cauliflower, optional
- 1 packet mushrooms
- 300 g minced meat
- 1 tbsp yoghurt
- 1/2 cup milk
- Shredded cheese, optional; quantity not specified

#### Method

1. Stir-fry the onion, garlic, and tomato until softened. Add the mushrooms and minced meat and cook through.
2. Add the yoghurt, milk, and optional cheese for the final 2 minutes.

#### Notes

- The source lists bottled pasta sauce and optional cauliflower but does not state when to add them. Bottle and packet sizes are not specified.
- Pasta quantity and cooking instructions are not provided.

#### Source

Supplied recipe document.

<a id="tomato-pasta-sauce-homemade"></a>

### Homemade tomato pasta sauce

**ID:** `tomato-pasta-sauce-homemade`

**Servings:** 5 portions.

**Time:** Yoghurt, milk, and optional cheese: final 2 minutes. Other times not specified.

**Review:** Imported draft.

#### Ingredients

- 2 tomatoes, diced
- 100 g pumpkin
- 2 apples
- 1 carrot
- 100 g cauliflower
- 1 sprig basil leaves
- 3/4 cup boiled red lentils
- 1 tsp Italian herbs
- 1 onion, diced
- Garlic: 4, minced; unit not specified
- 1 packet mushrooms
- 2 tbsp yoghurt
- 1/2 cup milk
- Shredded cheese, quantity not specified, or 1 slice cheese; optional
- 1.5 tubes tofu or 150 g meat

#### Method

1. Stir-fry the onion, garlic, and vegetables until softened.
2. Add the yoghurt, milk, and optional cheese for the final 2 minutes.
3. Blend when cooled.

#### Notes

- The source does not state when to add the apples, basil, lentils, Italian herbs, or tofu/meat, or how to cook the meat option.
- Tofu tube and mushroom packet sizes, pasta quantity, and pasta cooking instructions are not provided.

#### Source

Supplied recipe document.

<a id="bolognese-pasta"></a>

### Bolognese pasta

**ID:** `bolognese-pasta`

**Servings:** 5 portions.

**Time:** Sauce: simmer for 30 minutes, or until vegetables are soft. Eggs: boil for 8 minutes.

**Review:** Imported draft.

#### Ingredients

- 4 garlic cloves, minced
- 1 large onion, diced
- 1 carrot, diced
- 1/2 packet raisins
- 1 celery stalk, outer layer removed, sliced diagonally and diced
- 1/2 packet mushrooms
- 1 tbsp Italian herbs
- 1 basil leaf
- 2 large tomatoes, peeled and cubed
- 200 g minced beef
- 1 bottle pasta sauce
- 1 to 2 tbsp tomato paste, optional
- Mozzarella cheese, quantity not specified
- 2 to 3 tbsp milk
- 1 broccoli, steamed, for serving
- 4 eggs, boiled for 8 minutes, for serving
- Pasta, quantity not specified

#### Method

1. Stir-fry the onion, garlic, minced beef, and mushrooms.
2. Add the carrot, celery, tomatoes, Italian herbs, and basil and fry until the tomatoes are soft.
3. Add the bottled pasta sauce and simmer for 30 minutes, or until all the vegetables are soft.
4. When ready, add the milk and some cheese. Taste and add tomato paste for more flavour if needed; skip it if already tasty.
5. Serve with the steamed broccoli and eggs boiled for 8 minutes.

#### Notes

- The raisins are listed without an addition step. Pasta quantity and cooking instructions are not specified.
- The source calls the eggs "half boiled" while specifying 8 minutes; both details are retained for review.

#### Source

Supplied recipe document.

<a id="creamy-chicken-macaroni-soup"></a>

### Creamy chicken macaroni soup

**ID:** `creamy-chicken-macaroni-soup`

**Servings:** 5 portions.

**Time:** Covered simmer: 20 minutes. After adding stock: 5 minutes, or until vegetables are soft.

**Review:** Imported draft.

#### Ingredients

- 1/2 packet brown mushrooms
- 1/2 onion, diced
- 1 carrot, diced
- 1 celery stick, outer layer removed and diced
- 1 leek
- Garlic: 4, minced; unit not specified
- 2 chicken fillets, cut into large cubes
- 1 packet chicken stock
- 200 ml water, or enough to cover the vegetables
- Macaroni, quantity not specified
- 150 ml milk

#### Method

1. Lightly fry the ingredients, then add 200 ml water or enough to cover the vegetables. Cover the pot and simmer for 20 minutes.
2. Add the chicken stock and bring to a boil. Simmer for 5 minutes, or until the vegetables are soft.
3. Cook the macaroni separately until about three-quarters cooked, then stir it into the pot.
4. Add 150 ml milk and serve.

#### Notes

- The source does not specify the chicken stock packet volume or macaroni quantity. It does not state a final cooking duration after the partly cooked macaroni is added.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.instagram.com/reel/C8T2t_3Svcs/)

<a id="japanese-sushi-onigiri"></a>

### Japanese sushi and onigiri

**ID:** `japanese-sushi-onigiri`

**Servings:** 5 portions.

**Time:** Salmon: bake for 10 minutes. Carrots: steam for 5 minutes. Zucchini and crab sticks: steam for 3 minutes each.

**Review:** Imported draft.

#### Ingredients

- Salmon mayo filling: 600 g salmon, described as 2.5 pieces
- Salmon mayo filling: 2 tsp sesame oil
- Salmon mayo filling: 1.5 carrots, shredded
- Salmon mayo filling: 1.5 zucchini, shredded
- Salmon mayo filling: 1/2 packet crab sticks
- Salmon mayo filling: 1 tsp soy sauce
- Salmon mayo filling: 1 cube cream cheese
- Salmon mayo filling: 3 tbsp Greek yoghurt
- Salmon mayo filling: 1.5 tsp mayonnaise
- Japanese-style scrambled eggs: 4 eggs
- Japanese-style scrambled eggs: 1 tsp soy sauce
- Japanese-style scrambled eggs: 1/2 tsp dashi powder
- Japanese-style scrambled eggs: 1 tsp mirin
- Japanese-style scrambled eggs: 1 tsp water
- Rice: 1.5 cups Japanese rice
- Rice: 2 packets furikake
- Rice: 1.5 tbsp apple cider vinegar
- Rice: 1.5 tbsp mirin, non-alcoholic as specified in the source
- Seaweed, for serving; quantity not specified
- Pork floss, for serving; quantity not specified

#### Method

1. Bake the salmon with 2 tsp sesame oil at 180 degrees for 10 minutes. The temperature scale is not specified.
2. Steam the shredded carrots for 5 minutes, zucchini for 3 minutes, and crab sticks for 3 minutes. Drain excess water from the carrots and zucchini using a strainer.
3. Mix the salmon, carrots, zucchini, and crab sticks with 1 tsp soy sauce, the cream cheese, Greek yoghurt, and mayonnaise.
4. Mix warm Japanese rice with the furikake, apple cider vinegar, and non-alcoholic mirin.
5. Serve with rice, seaweed, and pork floss.

#### Notes

- The oven temperature is stated as 180 degrees without Celsius or Fahrenheit.
- The source supplies ingredients for Japanese-style scrambled eggs but gives no cooking method. Sushi rolling and onigiri shaping instructions are also not provided.
- Cream cheese cube and furikake packet sizes are not specified. The source does not say whether the rice quantity is measured before or after cooking.

#### Source

Supplied recipe document.

<a id="korean-kimbap"></a>

### Korean kimbap

**ID:** `korean-kimbap`

**Servings:** 5 portions.

**Time:** Carrot: steam for 5 minutes. Other times not specified.

**Review:** Imported draft.

#### Ingredients

- 1/3 cup mixed-grain rice
- 2/3 cup Japanese rice
- 1 tbsp sesame oil
- Sesame seed powder, quantity not specified
- 3 small sheets Korean salted seaweed
- 1 can tuna, drained in a strainer
- 1/2 carrot, shredded
- 1/3 bowl corn
- Boiled egg, optional; quantity not specified
- 1 tsp soy sauce
- 2 tbsp Greek yoghurt
- 1 tsp mayonnaise

#### Method

1. Mix the warm rice with sesame oil, sesame seed powder, and the Korean salted seaweed.
2. Steam the shredded carrot for 5 minutes. Drain excess water from the tuna.
3. Mix the tuna, carrot, corn, and optional boiled egg with soy sauce, Greek yoghurt, and mayonnaise.

#### Notes

- The source does not provide rolling or assembly instructions. It does not specify whether the rice quantities are measured before or after cooking.
- The source's "mix all of the above" follows the filling ingredients; interpreted here as the filling, separately from the seasoned rice. Confirm this scope.

#### Source

Supplied recipe document.

- [Original recipe link](https://www.instagram.com/reel/C6GjWiwLOMb/)

<a id="mexican-wraps"></a>

### Mexican wraps

**ID:** `mexican-wraps`

**Servings:** 5 portions.

**Time:** Cheese bake: about 8 minutes. Other times not specified.

**Review:** Imported draft.

#### Ingredients

- Beef filling: 400 g fresh minced beef
- Beef filling: 1 onion, finely diced
- Beef filling: 2 garlic cloves, minced
- Beef filling: 2 tbsp tomato paste
- Beef filling: 50 ml water
- Beef filling: black pepper, a sprinkle
- Beef filling: 1 tsp all-purpose seasoning, or 1 tsp paprika plus 1 tsp mushroom salt
- Beef filling: 1 tsp oregano or Italian herbs
- Beef filling: 1 tsp garlic powder
- Beef filling: 1 tsp onion powder
- Beef filling: 1 tbsp oil
- Beef filling: cheese for baking, type and quantity not specified
- Tofu scrambled eggs: 6 eggs
- Tofu scrambled eggs: 1/2 packet silken tofu
- Tofu scrambled eggs: mozzarella cheese, quantity not specified
- Tofu scrambled eggs: salt, a sprinkle
- Tofu scrambled eggs: 1 tbsp milk
- Tofu scrambled eggs: butter, quantity not specified
- Guacamole: 1 avocado
- Guacamole: 2 tbsp Greek yoghurt
- Guacamole: juice of 1/2 lime
- Guacamole: salt, a sprinkle
- Guacamole: 1 tsp garlic powder
- Guacamole: 1 shallot
- Guacamole: 1/2 packet baby tomatoes, cubed
- Gardenia wraps or hard-shell tacos, for serving; quantity not specified
- Shredded carrots, for serving; quantity not specified
- Mesclun salad, for serving; quantity not specified
- Fish fingers, optional, for serving; quantity not specified

#### Method

1. For the beef filling, stir-fry the onion and garlic in 1 tbsp oil until slightly softened. Add the beef and fry until it turns light brown.
2. Add the seasoning and mix well until the beef is cooked. Add tomato paste and water and cook until the water evaporates, leaving a juicy filling rather than a watery one.
3. Bake with cheese for about 8 minutes, until melted.
4. For the tofu scrambled eggs, cook the eggs, silken tofu, mozzarella, salt, and milk with butter.
5. Serve with wraps or hard-shell tacos, shredded carrots, mesclun salad, and optional fish fingers.

#### Notes

- The source lists guacamole ingredients without a preparation method.
- The baking temperature and exactly what is baked with the cheese are not specified. The wrap assembly method and fish finger preparation are also not given.

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

1. Bake the salmon with herbs at 180 degrees for 8 minutes. The temperature scale is not specified.
2. Microwave the peeled sweet potato for 7 minutes. Microwave the broccoli and grated carrot or zucchini for 3 minutes. Blend the cooked vegetables.
3. Mix the salmon, blended vegetables, and the stated oat or wholemeal flour well. The oat form is unclear. The egg is listed in the source but its addition is not stated.
4. Bake for 30 minutes at 180 degrees. The temperature scale is not specified.

#### Notes

- Both oven temperatures are written as 180 degrees without Celsius or Fahrenheit. Microwave power is not specified.
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

1. Roll into balls and bake for 20 minutes at 180 degrees. The temperature scale is not specified.
2. Remove from the oven and pan-fry both sides for 3 minutes per side, or until slightly browned.

#### Notes

- A personal note in the source appears immediately before the breadcrumbs, mozzarella, and salt. Names were removed. Confirm whether these ingredients describe a separate variation and whether the following method applies to all variations.
- The method changes the description from balls to nuggets. Shape is not otherwise specified.
- The source gives no explicit mixing step, and the oven temperature scale is not specified.

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

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 6 scoops rice; scoop size and whether measured before or after cooking are not specified
- Minced chicken, quantity not specified
- 1/2 tsp cornstarch, for marinating the chicken
- 1 tsp sesame oil, for marinating the chicken
- Minced garlic, quantity not specified
- Shallot, quantity not specified
- Carrot, shredded; quantity not specified
- Cabbage, shredded; quantity not specified
- 1 egg
- 1 tsp soy sauce; specific formulation not provided

#### Method

1. Cook the rice.
2. Marinate the minced chicken with cornstarch and sesame oil.
3. Fry the minced garlic and shallot with the shredded carrot and cabbage until soft.
4. Scramble 1 egg.
5. Fry the rice with all the ingredients and add 1 tsp soy sauce.

#### Notes

- The original soy sauce entry has a personal attribution, which was removed. Its formulation is not provided; confirm whether it refers to a specific homemade sauce.
- The source does not state how or when to cook the marinated chicken before combining the ingredients. The rice scoop size is not specified.

#### Source

Supplied recipe document.

## Archive

<a id="tomato-egg-soup-mee-sua"></a>

### Tomato egg soup with mee sua

**ID:** `tomato-egg-soup-mee-sua`

**Servings:** 5 portions.

**Time:** Not specified.

**Review:** Imported draft.

#### Ingredients

- 5 large tomatoes, cubed
- 2 garlic cloves, minced
- 4 eggs
- 1 large shallot
- 1 packet chicken stock, 1 litre
- White part of spring onion, mentioned in the method; quantity not specified
- 250 g sliced fish
- 1 tsp light soy sauce, for marinating the fish
- Cornstarch, for marinating the fish; quantity not specified
- 1 tsp sesame oil, for marinating the fish
- 1 small bowl chopped corn, steamed
- 1 packet mushrooms
- 1 packet leafy vegetables
- 2 bundles mee sua or soya mee
- 1 box silken tofu
- 1 tbsp oyster sauce and 1 tbsp ketchup, optional, after tasting

#### Method

1. Season the sliced fish with light soy sauce, cornstarch, and sesame oil. Steam the chopped corn.
2. For the soup, fry the garlic, shallot, and white spring onion. Add the cubed tomatoes and fry until paste-like.
3. Add the chicken stock and bring to a boil. Taste and add the optional oyster sauce and ketchup if needed.
4. Serve with the listed fish, corn, mushrooms, leafy vegetables, noodles, and tofu.

#### Notes

- This recipe remains in Archive, as in the source.
- The source does not specify when to add the 4 eggs, how to cook the fish, mushrooms, leafy vegetables, or noodles, or when to add the tofu. The final serving step does not resolve these gaps.

#### Source

Supplied recipe document.
