# Products Documentation

## Overview
The Products module is the heart of your Saleor store, enabling you to create, manage, and optimize your product catalog. Support for simple products, variants, grouped products, digital items, and services.

## Product Types

### Simple Products
- **Single SKU**: One product, one price
- **Use Cases**: Books, unique items, services
- **Quick Setup**: Minimal configuration needed

### Variable Products
- **Multiple Variants**: Size, color, material options
- **Shared Attributes**: Common base properties
- **Individual SKUs**: Each variant has unique identifier
- **Stock Tracking**: Per-variant inventory

### Grouped Products
- **Product Bundles**: Sell multiple items together
- **Related Sets**: Kitchen sets, gift baskets
- **Component Management**: Track individual items
- **Pricing Options**: Fixed or calculated bundle price

### Digital Products
- **Downloadable**: Files, software, media
- **License Keys**: Automated delivery
- **Access Control**: Download limits and expiry
- **No Shipping**: Instant delivery

### Service Products
- **Appointments**: Bookings and reservations
- **Subscriptions**: Recurring products
- **Custom Work**: Personalized services

## Creating Products

### Step-by-Step Process
1. Navigate to Catalog → Products → Add Product
2. Select product type
3. Enter basic information
4. Configure variants (if applicable)
5. Set pricing and tax
6. Add media and descriptions
7. Configure SEO settings
8. Publish or save as draft

### Required Fields
- **Product Name**: Unique, descriptive title
- **Product Type**: Defines attribute structure
- **Category**: Primary classification
- **SKU**: Stock keeping unit
- **Price**: Base pricing

### Optional Fields
- **Description**: Rich text editor
- **Weight/Dimensions**: For shipping
- **Metadata**: Custom fields
- **Tags**: For organization
- **Related Products**: Cross-selling

## Product Variants

### Creating Variants
1. **Define Attributes**: Size, color, material
2. **Generate Combinations**: Automatic or manual
3. **Set Individual Prices**: Override base price
4. **Manage Stock**: Per-variant inventory
5. **Unique SKUs**: For each combination

### Variant Management
- **Bulk Edit**: Update multiple variants
- **Quick Actions**: Enable/disable variants
- **Stock Sync**: Update inventory levels
- **Price Adjustments**: Percentage or fixed

### Variant Options
| Attribute | Examples | Type |
|-----------|----------|------|
| Size | S, M, L, XL | Dropdown |
| Color | Red, Blue, Green | Color Picker |
| Material | Cotton, Polyester | Selection |
| Style | Regular, Slim, Relaxed | Radio |
| Custom | Any attribute | Text/Number |

## Grouped Products Configuration

### Bundle Creation
1. **Create Parent Product**: Main bundle item
2. **Add Components**: Select products to include
3. **Set Quantities**: How many of each
4. **Configure Pricing**:
   - **Fixed Price**: Set bundle price
   - **Sum of Components**: Calculate automatically
   - **Discount**: Percentage off total

### Bundle Management
- **Component Stock**: Track individually
- **Availability Rules**: All must be in stock
- **Substitutions**: Allow alternatives
- **Custom Bundles**: Customer-selected items

### Bundle Types
- **Fixed Bundles**: Pre-defined sets
- **Mix & Match**: Customer chooses items
- **Tiered Bundles**: Different package levels
- **Gift Sets**: Special packaging options

## Product Media

### Image Requirements
- **Format**: JPEG, PNG, WebP
- **Size**: Max 10MB per image
- **Resolution**: Minimum 800x800px
- **Aspect Ratio**: Square recommended

### Media Types
- **Main Image**: Primary product photo
- **Gallery Images**: Multiple angles
- **Variant Images**: Specific to variants
- **Videos**: Product demonstrations
- **360° Views**: Interactive images
- **Documents**: PDFs, manuals

### Image Optimization
1. Use high-quality originals
2. Compress for web
3. Add alt text for SEO
4. Use consistent styling
5. Show scale/context

## Pricing & Tax

### Pricing Strategies
- **Regular Price**: Standard selling price
- **Sale Price**: Temporary reductions
- **Tiered Pricing**: Volume discounts
- **Customer Group Pricing**: B2B/B2C different rates
- **Currency-specific**: Multi-currency support

### Tax Configuration
- **Tax Class**: Standard, reduced, zero
- **Tax Included**: Gross pricing
- **Tax Excluded**: Net pricing
- **Regional Rules**: Country/state specific

## Inventory Management

### Stock Tracking
- **Track Inventory**: Enable/disable
- **Stock Quantity**: Current levels
- **Low Stock Threshold**: Alert levels
- **Backorders**: Allow/prevent
- **Reserved Stock**: For pending orders

### Stock Updates
- **Manual Update**: Direct entry
- **Bulk Import**: CSV upload
- **API Sync**: External systems
- **Automatic Adjustments**: Order processing

### Multi-warehouse
- **Location Management**: Multiple warehouses
- **Stock Allocation**: Per location
- **Transfer Orders**: Between locations
- **Fulfillment Rules**: Nearest warehouse

## SEO & Marketing

### SEO Settings
- **Meta Title**: Page title for search
- **Meta Description**: Search snippet
- **URL Slug**: Friendly URLs
- **Canonical URL**: Prevent duplicates
- **Schema Markup**: Rich snippets

### Marketing Features
- **Related Products**: Cross-sell items
- **Upsells**: Premium alternatives
- **Featured**: Homepage displays
- **Tags**: Organization and filtering
- **Collections**: Curated groups

## Product Import/Export

### Import Process
1. Download template CSV
2. Fill product data
3. Upload CSV file
4. Map fields
5. Review and confirm
6. Process import

### Export Options
- **Format**: CSV, XLSX, JSON
- **Filters**: Category, status, date
- **Fields**: Select specific data
- **Schedule**: Automated exports

## Common Issues and Solutions

### "Product Not Showing"
- **Cause**: Not published or out of stock
- **Solution**:
  1. Check product status (Published)
  2. Verify stock levels
  3. Check category assignment
  4. Review visibility settings

### "Variants Not Generating"
- **Cause**: Attribute configuration issue
- **Solution**:
  1. Verify attribute values assigned
  2. Check variant generation settings
  3. Manually create if needed
  4. Review product type configuration

### "Images Not Displaying"
- **Cause**: File size, format, or upload error
- **Solution**:
  1. Check image format (JPEG, PNG)
  2. Verify file size (<10MB)
  3. Re-upload images
  4. Clear CDN cache

## Best Practices

1. **Complete Information**: Fill all relevant fields
2. **High-Quality Images**: Multiple angles, zoom capability
3. **Clear Descriptions**: Features, benefits, specifications
4. **Accurate Stock**: Regular inventory updates
5. **SEO Optimization**: Unique titles and descriptions
6. **Regular Reviews**: Update pricing and availability
7. **Variant Organization**: Logical attribute structure
8. **Bundle Strategy**: Create value through grouping

## Advanced Features

### Product Automation
- **Auto-publish**: Schedule product launches
- **Price Rules**: Dynamic pricing
- **Stock Alerts**: Low inventory notifications
- **Variant Generation**: Bulk create options

### Integration Options
- **PIM Systems**: Product information management
- **ERP Sync**: Enterprise resource planning
- **Dropshipping**: Supplier integration
- **Marketplace Sync**: Multi-channel selling