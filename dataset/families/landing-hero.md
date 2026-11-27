# Family: landing / hero page

Status: **draft**, derived from 9 records (batches 03 and 04). Treat as hypotheses until more records are added and the owner has reviewed them.

## Records
| ID | Hero visual | Primary action | Final | Access. | Critical |
|---|---|---|---|---|---|
| vixen-ui-020 | fan of artwork cards with creator chips | black pill 'Join for $9.99/m' plus a text link | 75.0 | 3 | - |
| vixen-ui-021 | cut-out model over a coral panel, oversized headlines | 'New Drops' pill and a featured-product card | 64.0 | 1 | CF1? |
| vixen-ui-032 | radial glow and proof tiles | 'GET IN TOUCH' pill | 77.0 | 4 | - |
| vixen-ui-034 | illustration and a timeline footer | none (hamburger menu only) | 61.0 | 1 | CF1? |
| vixen-ui-035 | 3D tile row and class cards | two pills (Contact Us, Join us) | 71.0 | 2 | - |
| vixen-ui-036 | cut-out figure with occluded wordmark | none (scroll cue only) | 59.0 | 1 | CF1 |
| vixen-ui-040 | product bar mock on a landscape photo | none shown | 71.0 | 4 | - |
| vixen-ui-043 | fan of character-colored cards | none shown | 59.0 | 1 | CF1 |
| vixen-ui-045 | building photo, search bar, scooped corner | purple 'Search' button (and a green 'Book Now' tag) | 56.0 | 1 | CF1 |

## Invariants
- A large headline as the first read.
- One dominant visual that is not a photo of the product alone: a fan of cards, a cut-out subject, an illustration, a glow, a product mock, or a photo with a search bar.
- A restrained palette driven by one brand or content color.

## Variations and what the measurements show
1. **Primary action.** Four of 9 records show no primary action (034, 036, 040, 043); one shows two pills of equal weight (035); one has a primary action plus a second primary-looking tag (045).
2. **Text on brand fields.** 5 of 9 records have a primary label below 3:1 (vixen-ui-021, vixen-ui-034, vixen-ui-036, vixen-ui-043, vixen-ui-045), typically white or pale text on a mid-tone brand color (coral, blue, orange). The records without one are vixen-ui-020, vixen-ui-032, vixen-ui-035, vixen-ui-040.
3. **Content and copy.** Copy or data that contradicts the product appears in 045 (ad-platform service cards and tech logos on a real-estate page) and 040 (the forecast repeats 'Thu / 30°' three times and the ring has no label).
4. **Orientation.** 021 asks phone users to rotate the device instead of reflowing the layout.
5. **Overlap devices** (cut-out over a panel or occluded wordmark: 021, 036; card fan: 020, 043) add depth; the fan in 043 hides the card titles.
6. **Proof.** Real, on-topic proof is shown as stats and logos in 032, a priced offer in 020 and community counts in 035.

## Draft defaults for a hero (to be validated)
- State the offer in the headline and give one dominant primary action.
- Check every text line placed on a brand color; white on these coral, blue and orange fields measured about 2.2 to 2.8:1.
- Use proof that matches the product; review placeholder copy and logos.
- Make the layout respond to the viewport instead of locking an orientation.
- Use an overlap device only for decorative regions, never over titles or text.
- Show at least a hover and focus state for the main action.

## Build notes
Effort is mostly Medium: layered cut-outs, masks or transforms and asset-heavy images (see each record's `build`).
