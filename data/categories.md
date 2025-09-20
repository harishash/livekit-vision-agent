# Categories Documentation

## Overview
Categories provide the hierarchical structure for organizing your product catalog, enabling intuitive navigation and improving the shopping experience. Create multi-level category trees with SEO-optimized pages.

## Category Structure

### Hierarchy Levels
- **Root Categories**: Top-level categories (e.g., Clothing, Electronics)
- **Parent Categories**: Main groupings (e.g., Men's, Women's)
- **Subcategories**: Specific divisions (e.g., Shirts, Pants)
- **Deep Nesting**: Up to 5 levels supported

### Category Types
- **Standard Categories**: Regular product groupings
- **Virtual Categories**: Dynamic product assignment
- **Hidden Categories**: Backend organization only
- **Seasonal Categories**: Time-based visibility

## Creating Categories

### Step-by-Step Process
1. Navigate to Catalog → Categories
2. Click "Add Category" or "Add Subcategory"
3. Enter category name and slug
4. Select parent category (if subcategory)
5. Add description and images
6. Configure SEO settings
7. Set visibility and status
8. Save and publish

### Required Information
- **Category Name**: Display name
- **URL Slug**: SEO-friendly URL
- **Parent Category**: For subcategories
- **Sort Order**: Display position

### Optional Settings
- **Description**: Category page content
- **Banner Image**: Hero image
- **Thumbnail**: Navigation image
- **Meta Data**: SEO information
- **Custom Attributes**: Additional fields

## Category Management

### Bulk Operations
- **Move Categories**: Reorganize hierarchy
- **Merge Categories**: Combine duplicates
- **Delete Categories**: With product reassignment
- **Export/Import**: CSV operations

### Category Assignment
- **Manual Assignment**: Product by product
- **Bulk Assignment**: Multiple products
- **Rules-based**: Automatic assignment
- **Inheritance**: From parent categories

## Navigation Configuration

### Menu Structure
- **Main Navigation**: Primary categories
- **Mega Menu**: Multi-column dropdowns
- **Sidebar Navigation**: Category trees
- **Breadcrumbs**: Path navigation
- **Footer Links**: Category shortcuts

### Display Options
| Setting | Options | Impact |
|---------|---------|--------|
| Sort Order | Manual, Alphabetical, Popular | Category arrangement |
| Product Count | Show/Hide | Display item numbers |
| Empty Categories | Show/Hide | Visibility of empty |
| Depth | 1-5 levels | Navigation complexity |
| Columns | 1-4 | Mega menu layout |

## Category Pages

### Page Elements
- **Header**: Category name and breadcrumbs
- **Banner**: Promotional images
- **Description**: Category information
- **Filters**: Product refinement
- **Products**: Grid or list view
- **Pagination**: Page navigation

### Customization Options
- **Layout**: Grid, list, or custom
- **Products per Page**: 12, 24, 48, 96
- **Sort Options**: Price, name, popularity
- **Filter Position**: Sidebar or top
- **Mobile View**: Responsive design

## SEO Optimization

### Category SEO
- **Meta Title**: Search engine title
- **Meta Description**: Search snippet
- **H1 Tag**: Page heading
- **URL Structure**: /category/subcategory
- **Canonical URLs**: Prevent duplicates

### Best Practices
1. Use descriptive category names
2. Create unique descriptions
3. Optimize URL slugs
4. Add schema markup
5. Include keywords naturally

## Category Filters

### Filter Types
- **Price Range**: Min/max sliders
- **Brands**: Manufacturer filter
- **Attributes**: Size, color, etc.
- **Availability**: In stock only
- **Ratings**: Customer reviews
- **Tags**: Custom labels

### Filter Configuration
1. Select applicable filters
2. Set filter order
3. Configure display type
4. Set default values
5. Enable on category

## Category Rules

### Dynamic Categories
- **Condition-based**: Automatic product inclusion
- **Rule Types**: Price, brand, attribute
- **Combinations**: AND/OR logic
- **Schedule**: Time-based rules
- **Priority**: Rule execution order

### Rule Examples
```
IF product.price > 100 AND product.brand = "Premium"
THEN assign to "Luxury Items"

IF product.tag contains "sale" AND product.stock > 0
THEN assign to "Current Deals"
```

## Performance Optimization

### Caching Strategies
- **Page Cache**: Full page caching
- **Fragment Cache**: Component caching
- **CDN Integration**: Static assets
- **Database Indexes**: Query optimization

### Loading Optimization
- **Lazy Loading**: Images and products
- **Pagination**: Limit initial load
- **Progressive Enhancement**: Core first
- **Minification**: CSS and JavaScript

## Common Issues and Solutions

### "Category Not Showing"
- **Cause**: Visibility settings or no products
- **Solution**:
  1. Check category status (Active)
  2. Verify visibility settings
  3. Ensure products assigned
  4. Check navigation menu settings

### "Products in Wrong Category"
- **Cause**: Incorrect assignment or inheritance
- **Solution**:
  1. Review product categories
  2. Check inheritance rules
  3. Verify dynamic rules
  4. Bulk reassign if needed

### "Slow Category Pages"
- **Cause**: Too many products or filters
- **Solution**:
  1. Enable pagination
  2. Optimize images
  3. Reduce filter options
  4. Enable caching

### "Duplicate Categories"
- **Cause**: Import errors or manual creation
- **Solution**:
  1. Identify duplicates
  2. Merge categories
  3. Redirect old URLs
  4. Update products

## Category Analytics

### Metrics to Track
- **Page Views**: Category popularity
- **Conversion Rate**: Category performance
- **Bounce Rate**: Engagement level
- **Average Time**: User interest
- **Exit Rate**: Navigation issues

### Optimization Strategies
- A/B test layouts
- Refine filter options
- Improve descriptions
- Optimize product order
- Enhance imagery

## Best Practices

1. **Logical Structure**: Intuitive hierarchy
2. **Consistent Naming**: Clear conventions
3. **Balanced Depth**: Not too deep (max 3-4 levels)
4. **Unique Content**: Avoid duplicate descriptions
5. **Regular Review**: Prune empty categories
6. **Mobile-First**: Responsive design
7. **SEO Focus**: Optimized metadata
8. **Performance**: Fast loading times

## Integration Features

### API Access
- GraphQL queries for categories
- REST endpoints
- Webhook events
- Bulk operations

### Third-Party Integration
- Google Shopping categories
- Facebook catalog
- Marketplace mapping
- PIM systems

## Advanced Features

### Multi-Store Categories
- **Shared Structure**: Common categories
- **Store-Specific**: Unique per store
- **Localization**: Translated names
- **Regional Variations**: Country-specific

### Category Permissions
- **View Permissions**: Customer group based
- **Edit Permissions**: Staff roles
- **Private Categories**: B2B catalogues
- **Approval Workflow**: Category changes