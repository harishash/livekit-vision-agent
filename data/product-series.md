# Product Series Documentation

## Overview
Product Series (Collections) allow you to group related products together for marketing, merchandising, and organizational purposes. Create curated collections, seasonal campaigns, brand showcases, and thematic product groups.

## Series Types

### Manual Collections
- **Hand-picked Products**: Curated selection
- **Custom Order**: Arrange products manually
- **Full Control**: Add/remove anytime
- **Use Cases**: Featured items, staff picks, gift guides

### Automated Collections
- **Rule-based**: Dynamic product inclusion
- **Auto-update**: Products added/removed automatically
- **Condition-driven**: Price, tags, inventory, attributes
- **Use Cases**: Sale items, new arrivals, bestsellers

### Hybrid Collections
- **Combined Approach**: Rules plus manual additions
- **Override Options**: Exclude specific products
- **Pinned Products**: Always show certain items
- **Use Cases**: Seasonal with featured items

## Creating Product Series

### Step-by-Step Process
1. Navigate to Catalog → Product Series
2. Click "Create New Series"
3. Enter series name and description
4. Choose collection type (Manual/Automated)
5. Set up rules or select products
6. Configure display settings
7. Add imagery and SEO data
8. Publish series

### Required Fields
- **Series Name**: Display title
- **URL Slug**: Web address
- **Type**: Manual or Automated
- **Status**: Active/Draft/Scheduled

### Optional Configuration
- **Description**: Rich text content
- **Hero Image**: Collection banner
- **Thumbnail**: Grid display image
- **Sort Order**: Product arrangement
- **Visibility**: Public/Private/Specific groups

## Automated Rules

### Rule Conditions
| Condition | Operators | Example |
|-----------|-----------|---------|
| Product Title | Contains, Starts with, Ends with | Title contains "Summer" |
| Price | Greater than, Less than, Between | Price > $50 |
| Inventory | In stock, Out of stock, Low stock | Stock > 10 |
| Category | Is, Is not, In any of | Category is "Shoes" |
| Tags | Has tag, Doesn't have tag | Has tag "bestseller" |
| Brand | Equals, Not equals | Brand = "Nike" |
| Created Date | Before, After, Between | Created after 30 days ago |
| Attributes | Has value, Doesn't have | Color = "Red" |

### Rule Combinations
- **ALL Conditions (AND)**: Must match all rules
- **ANY Conditions (OR)**: Match at least one rule
- **Complex Logic**: Nested rule groups
- **Exclusions**: Specific products to never include

### Rule Examples
```
// Summer Sale Collection
IF product.tags CONTAINS "summer" 
AND product.discount > 20%
AND product.stock > 0

// New Arrivals
IF product.created_date > 7_days_ago
AND product.status = "active"

// Premium Products
IF product.price > 200
OR product.brand IN ["Luxury1", "Premium2"]
AND product.rating >= 4.5
```

## Series Management

### Product Management
- **Add Products**: Search and select
- **Bulk Add**: CSV import or category
- **Remove Products**: Individual or bulk
- **Reorder**: Drag and drop
- **Pin Products**: Always show first

### Display Settings
- **Layout**: Grid, list, carousel
- **Products per Page**: 12, 24, 48
- **Sort Options**: Manual, price, name, newest
- **Default Sort**: Initial display order
- **Mobile Layout**: Responsive options

## Series Page Customization

### Page Sections
- **Header**: Title, description, breadcrumbs
- **Hero Section**: Banner image or slider
- **Filters**: Product refinement options
- **Product Grid**: Item display
- **Pagination**: Navigation controls
- **Related Series**: Cross-promotion

### Design Options
- **Templates**: Pre-built layouts
- **Custom CSS**: Advanced styling
- **Widgets**: Add promotional blocks
- **Rich Content**: HTML descriptions
- **Video Headers**: Engaging media

## Marketing Features

### Promotional Tools
- **Badges**: "New", "Sale", "Exclusive"
- **Countdown Timers**: Limited time offers
- **Stock Indicators**: Urgency messaging
- **Social Proof**: View/purchase counts
- **Quick View**: Product preview

### Cross-Selling
- **Related Series**: Similar collections
- **Recommended Products**: AI suggestions
- **Recently Viewed**: Personalization
- **Bundle Offers**: Series-wide discounts

## SEO & Discovery

### SEO Settings
- **Meta Title**: Search engine title
- **Meta Description**: Search snippet
- **Open Graph**: Social media sharing
- **Schema Markup**: Rich snippets
- **Sitemap**: Search engine indexing

### Internal Linking
- **Navigation Menus**: Primary placement
- **Homepage Features**: Carousel/grid
- **Category Pages**: Related collections
- **Product Pages**: Collection badges
- **Footer Links**: Quick access

## Scheduling & Visibility

### Time-Based Display
- **Start Date**: When to show
- **End Date**: When to hide
- **Time Zone**: Store timezone
- **Preview Mode**: Test before launch

### Visibility Rules
- **Customer Groups**: B2B, VIP, Members
- **Geographic**: Country/region specific
- **Device Type**: Mobile/Desktop only
- **Login Status**: Guest vs. registered

## Performance Optimization

### Loading Strategies
- **Lazy Loading**: Progressive image loading
- **Pagination**: Limit initial products
- **Caching**: Static content caching
- **CDN**: Content delivery network
- **Compression**: Image optimization

### Best Practices
1. Limit products per page (24-48)
2. Optimize hero images (<500KB)
3. Use thumbnail previews
4. Enable browser caching
5. Minimize rule complexity

## Analytics & Reporting

### Metrics to Track
- **Views**: Collection page visits
- **Conversion Rate**: Views to purchases
- **Revenue**: Sales from collection
- **Popular Products**: Top performers
- **Engagement**: Time on page

### A/B Testing
- Test different layouts
- Compare hero images
- Vary product counts
- Try sort orders
- Measure CTAs

## Common Issues and Solutions

### "Products Not Showing"
- **Cause**: Rule mismatch or stock issues
- **Solution**:
  1. Review rule conditions
  2. Check product attributes
  3. Verify stock levels
  4. Test with broader rules

### "Slow Loading Series"
- **Cause**: Too many products or large images
- **Solution**:
  1. Enable pagination
  2. Optimize images
  3. Reduce products shown
  4. Enable caching

### "Rules Not Working"
- **Cause**: Conflicting conditions or syntax
- **Solution**:
  1. Simplify rules
  2. Check AND/OR logic
  3. Test individual conditions
  4. Review exclusions

## Best Practices

1. **Clear Naming**: Descriptive series titles
2. **Compelling Imagery**: High-quality hero images
3. **Regular Updates**: Keep collections fresh
4. **Strategic Placement**: Prominent navigation
5. **Mobile Optimization**: Responsive design
6. **Rule Testing**: Verify automated rules
7. **Performance Monitoring**: Track loading times
8. **SEO Focus**: Unique descriptions

## Advanced Features

### API Integration
- GraphQL queries for collections
- Webhook notifications
- Bulk operations
- External sync

### Multi-Channel
- **Website**: Primary display
- **Mobile App**: App-specific series
- **Social Commerce**: Instagram/Facebook
- **Marketplaces**: Channel collections
- **Email**: Campaign integration

### Personalization
- **User Preferences**: Customized display
- **Browsing History**: Related suggestions
- **Purchase History**: Complementary items
- **Geographic**: Location-based series
- **Seasonal**: Time-relevant collections