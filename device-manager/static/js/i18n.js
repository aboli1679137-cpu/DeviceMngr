// i18n Translation System - English / Persian (Farsi)
const translations = {
  en: {
    // App
    'app.name': 'DeviceManager',
    'app.subtitle': 'Workspace Admin',
    'app.tagline': 'Professional Device Management System',

    // Navigation sections
    'nav.overview': 'Overview',
    'nav.dashboard': 'Dashboard',
    'nav.management': 'Management',
    'nav.add_system': 'Add System',
    'nav.all_systems': 'All Systems',
    'nav.categories': 'Categories',
    'nav.customer_systems': 'Customer Systems',
    'nav.for_sale': 'For Sale',
    'nav.internal_use': 'Internal Use',
    'nav.service': 'Service',
    'nav.repair_systems': 'Repair Systems',
    'nav.system': 'System',
    'nav.settings': 'Settings',

    // Status labels
    'status.READY': 'Ready',
    'status.IN_REPAIR': 'In Repair',
    'status.DAMAGED': 'Damaged',
    'status.DELIVERED': 'Delivered',
    'status.SOLD': 'Sold',
    'status.PENDING_INSPECTION': 'Pending Inspection',
    'status.TESTED': 'Tested',
    'status.ARCHIVED': 'Archived',

    // Repair status labels
    'repair_status.PENDING': 'Pending',
    'repair_status.IN_PROGRESS': 'In Progress',
    'repair_status.COMPLETED': 'Completed',
    'repair_status.CANCELLED': 'Cancelled',

    // Category labels
    'category.CUSTOMER': 'Customer System',
    'category.FOR_SALE': 'For Sale',
    'category.INTERNAL': 'Internal Use',

    // Subcategory labels
    'sub.TESTING': 'For Testing',
    'sub.SHOP_USE': 'For Shop/Internal Use',

    // Dashboard
    'dashboard.title': 'Dashboard',
    'dashboard.subtitle': 'Overview of your workspace',
    'dashboard.total': 'Total Systems',
    'dashboard.customer': 'Customer Systems',
    'dashboard.for_sale': 'For Sale',
    'dashboard.internal': 'Internal Use',
    'dashboard.damaged': 'Damaged',
    'dashboard.in_repair': 'In Repair',
    'dashboard.ready': 'Ready',
    'dashboard.recent_activity': 'Recent Activity',
    'dashboard.quick_actions': 'Quick Actions',
    'dashboard.view_all': 'View All',
    'dashboard.add_first': 'Add your first system',
    'dashboard.no_activity': 'No recent activity',

    // Add System
    'add.title': 'Register New System',
    'add.subtitle': 'Add a new computer system to the inventory',
    'add.basic_info': 'Basic Information',
    'add.hardware_specs': 'Hardware Specifications',
    'add.notes_section': 'Additional Notes',
    'add.system_name': 'System Name *',
    'add.serial_number': 'Serial Number',
    'add.customer_name': 'Customer Name',
    'add.customer_name_placeholder': 'Enter customer name or phone number',
    'add.date_of_entry': 'Date of Entry',
    'add.category': 'Category *',
    'add.status': 'Status',
    'add.subcategory': 'Subcategory *',
    'add.select_subcategory': 'Select subcategory...',
    'add.cancel': 'Cancel',
    'add.register': 'Register System',
    'add.saving': 'Saving...',
    'add.success': 'System registered successfully!',

    // Hardware fields
    'hw.cpu': 'CPU',
    'hw.ram': 'RAM',
    'hw.gpu': 'GPU',
    'hw.storage': 'Storage',
    'hw.motherboard': 'Motherboard',
    'hw.power_supply': 'Power Supply',
    'hw.case': 'Case',
    'hw.condition': 'Condition',
    'hw.placeholder.cpu': 'e.g. Intel Core i7-13700K',
    'hw.placeholder.ram': 'e.g. 32GB DDR5 5600MHz',
    'hw.placeholder.gpu': 'e.g. NVIDIA RTX 4070',
    'hw.placeholder.storage': 'e.g. 1TB NVMe SSD',
    'hw.placeholder.motherboard': 'e.g. ASUS ROG Z790',
    'hw.placeholder.psu': 'e.g. 850W Gold',
    'hw.placeholder.case': 'e.g. NZXT H5 Flow',
    'hw.placeholder.condition': 'e.g. Excellent, Good, Fair',
    'hw.placeholder.notes': 'Enter any additional notes or remarks about this system...',

    // All Systems
    'systems.title': 'All Systems',
    'systems.count': 'system(s) found',
    'systems.no_results': 'No systems found',
    'systems.adjust_filters': 'Try adjusting your search or filters',
    'systems.add_first': 'Start by adding your first system',
    'systems.search': 'Search by name, serial number, or hardware...',
    'systems.all_categories': 'All Categories',
    'systems.all_statuses': 'All Statuses',
    'systems.filters': 'Filters',
    'systems.clear_filters': 'Clear filters',

    // System detail
    'detail.system_info': 'System Info',
    'detail.hardware_specs': 'Hardware Specifications',
    'detail.notes': 'Notes',
    'detail.repair_history': 'Repair History',
    'detail.activity_log': 'Activity Log',
    'detail.quick_actions': 'Quick Actions',
    'detail.create_repair': 'Create Repair Record',
    'detail.repair_tip': 'Start a new repair ticket',
    'detail.entry_date': 'Entry Date',
    'detail.created': 'Created',
    'detail.last_updated': 'Last Updated',
    'detail.repairs': 'Repairs',
    'detail.activities': 'Activities',
    'detail.customer': 'Customer',
    'detail.not_found': 'System not found',
    'detail.confirm_delete': 'Are you sure? This cannot be undone.',
    'detail.delete_success': 'System deleted',

    // Repair
    'repair.title': 'Repair Center',
    'repair.count': 'repair record(s)',
    'repair.new_record': 'New Repair Record',
    'repair.create': 'Create Repair Record',
    'repair.edit': 'Edit Record',
    'repair.save': 'Save Changes',
    'repair.cancel': 'Cancel',
    'repair.no_records': 'No repair records found',
    'repair.select_device': 'Select Device *',
    'repair.choose_device': 'Choose a device...',
    'repair.issue_desc': 'Issue Description',
    'repair.symptoms': 'Observed Symptoms',
    'repair.probable_cause': 'Probable Cause',
    'repair.technician': 'Assigned Technician',
    'repair.status': 'Repair Status',
    'repair.cost': 'Repair Cost ($)',
    'repair.expected_completion': 'Expected Completion Date',
    'repair.completion_date': 'Completion Date',
    'repair.create_success': 'Repair record created',
    'repair.update_success': 'Repair record updated',

    // Repair detail
    'repair.detail.title': 'Repair Record',
    'repair.detail.details': 'Repair Details',
    'repair.detail.assignment': 'Assignment & Cost',
    'repair.detail.timeline': 'Timeline',
    'repair.detail.technician': 'Assigned Technician',
    'repair.detail.not_assigned': 'Not assigned',
    'repair.detail.cost': 'Repair Cost',
    'repair.detail.entry': 'Entry Date',
    'repair.detail.expected': 'Expected Completion',
    'repair.detail.completed': 'Completion Date',
    'repair.detail.no_details': 'No repair details recorded yet.',
    'repair.detail.not_found': 'Repair record not found',

    // Repair detail sections
    'repair_field.probable_cause': 'Probable Cause of Failure',
    'repair_field.issue_description': 'Issue Description',
    'repair_field.symptoms': 'Observed Symptoms',
    'repair_field.diagnostic_notes': 'Diagnostic Notes',
    'repair_field.checked_parts': 'Checked Parts',
    'repair_field.replaced_parts': 'Replaced Parts',
    'repair_field.repair_actions': 'Repair Actions Performed',
    'repair_field.tests_performed': 'Tests Performed',
    'repair_field.test_results': 'Test Results',
    'repair_field.technician_notes': 'Technician Notes',

    // Customer systems
    'customer.title': 'Customer Systems',
    'customer.no_results': 'No customer systems',
    'customer.desc': 'Systems owned by customers will appear here',

    // For sale
    'forsale.title': 'Systems For Sale',
    'forsale.no_results': 'No systems for sale',

    // Internal
    'internal.title': 'Internal Systems',
    'internal.all': 'All Internal Systems',
    'internal.no_results': 'No internal systems',

    // Settings
    'settings.title': 'Settings',
    'settings.subtitle': 'Manage your workspace preferences',
    'settings.appearance': 'Appearance',
    'settings.system': 'System',
    'settings.about': 'About',
    'settings.theme': 'Theme Mode',
    'settings.light': 'Light Mode',
    'settings.dark': 'Dark Mode',
    'settings.current_theme': 'Current: {theme}',
    'settings.database': 'Database',
    'settings.db_desc': 'SQLite (local)',
    'settings.application': 'Application',
    'settings.app_desc': 'DeviceManager v1.0.0',
    'settings.stack': 'Built with Flask · SQLite · Tailwind CSS',
    'settings.design': 'Designed for computer shops, repair centers, and technical workspaces',

    // Language
    'lang.en': 'English',
    'lang.fa': 'فارسی',
    'lang.switch': 'EN/FA',

    // Common
    'common.loading': 'Loading...',
    'common.failed': 'Failed to load data',
    'common.no_data': 'No data',
    'common.save': 'Save',
    'common.delete': 'Delete',
    'common.edit': 'Edit',
    'common.new': 'New',
    'common.back': 'Back',
    'common.confirm': 'Confirm',
    'common.search': 'Search',
    'common.s_n': 'S/N',
    'common.repairs': 'repair(s)',
    'common.no_repairs': 'No repairs',
    'common.tech': 'Tech',
    'common.cost': 'Cost',

    // Repair actions log
    'repair.log_action': 'Log Action',
    'repair.log_placeholder': 'Type action performed...',

    // Toast messages
    'toast.system_created': 'System registered successfully!',
    'toast.system_deleted': 'System deleted',
    'toast.status_updated': 'Status updated',
    'toast.repair_created': 'Repair record created',
    'toast.repair_updated': 'Repair record updated',
    'toast.failed': 'Operation failed',
    'toast.select_device': 'Please select a device',
  },

  fa: {
    // App
    'app.name': 'مدیریت دستگاه‌ها',
    'app.subtitle': 'مدیریت کارگاه',
    'app.tagline': 'سیستم حرفه‌ای مدیریت دستگاه‌ها',

    // Navigation sections
    'nav.overview': 'نمای کلی',
    'nav.dashboard': 'داشبورد',
    'nav.management': 'مدیریت',
    'nav.add_system': 'افزودن سیستم',
    'nav.all_systems': 'همه سیستم‌ها',
    'nav.categories': 'دسته‌بندی‌ها',
    'nav.customer_systems': 'سیستم‌های مشتری',
    'nav.for_sale': 'برای فروش',
    'nav.internal_use': 'استفاده داخلی',
    'nav.service': 'خدمات',
    'nav.repair_systems': 'سیستم‌های تعمیر',
    'nav.system': 'سیستم',
    'nav.settings': 'تنظیمات',

    // Status labels
    'status.READY': 'آماده',
    'status.IN_REPAIR': 'در حال تعمیر',
    'status.DAMAGED': 'خراب',
    'status.DELIVERED': 'تحویل شده',
    'status.SOLD': 'فروخته شده',
    'status.PENDING_INSPECTION': 'منتظر بازرسی',
    'status.TESTED': 'تست شده',
    'status.ARCHIVED': 'بایگانی شده',

    // Repair status labels
    'repair_status.PENDING': 'در انتظار',
    'repair_status.IN_PROGRESS': 'در حال انجام',
    'repair_status.COMPLETED': 'تکمیل شده',
    'repair_status.CANCELLED': 'لغو شده',

    // Category labels
    'category.CUSTOMER': 'سیستم مشتری',
    'category.FOR_SALE': 'برای فروش',
    'category.INTERNAL': 'استفاده داخلی',

    // Subcategory labels
    'sub.TESTING': 'برای تست',
    'sub.SHOP_USE': 'برای استفاده فروشگاه/داخلی',

    // Dashboard
    'dashboard.title': 'داشبورد',
    'dashboard.subtitle': 'نمای کلی کارگاه شما',
    'dashboard.total': 'مجموع سیستم‌ها',
    'dashboard.customer': 'سیستم‌های مشتری',
    'dashboard.for_sale': 'برای فروش',
    'dashboard.internal': 'استفاده داخلی',
    'dashboard.damaged': 'خراب',
    'dashboard.in_repair': 'در حال تعمیر',
    'dashboard.ready': 'آماده',
    'dashboard.recent_activity': 'فعالیت‌های اخیر',
    'dashboard.quick_actions': 'اقدامات سریع',
    'dashboard.view_all': 'مشاهده همه',
    'dashboard.add_first': 'اولین سیستم را اضافه کنید',
    'dashboard.no_activity': 'هیچ فعالیت اخیری وجود ندارد',

    // Add System
    'add.title': 'ثبت سیستم جدید',
    'add.subtitle': 'یک سیستم جدید به موجودی اضافه کنید',
    'add.basic_info': 'اطلاعات پایه',
    'add.hardware_specs': 'مشخصات سخت‌افزاری',
    'add.notes_section': 'یادداشت‌های اضافی',
    'add.system_name': 'نام سیستم *',
    'add.serial_number': 'شماره سریال',
    'add.customer_name': 'نام مشتری',
    'add.customer_name_placeholder': 'نام یا شماره تلفن مشتری را وارد کنید',
    'add.date_of_entry': 'تاریخ ورود',
    'add.category': 'دسته‌بندی *',
    'add.status': 'وضعیت',
    'add.subcategory': 'زیردسته *',
    'add.select_subcategory': 'زیردسته را انتخاب کنید...',
    'add.cancel': 'انصراف',
    'add.register': 'ثبت سیستم',
    'add.saving': 'در حال ذخیره...',
    'add.success': 'سیستم با موفقیت ثبت شد!',

    // Hardware fields
    'hw.cpu': 'پردازنده',
    'hw.ram': 'حافظه رم',
    'hw.gpu': 'کارت گرافیک',
    'hw.storage': 'فضای ذخیره‌سازی',
    'hw.motherboard': 'مادربرد',
    'hw.power_supply': 'منبع تغذیه',
    'hw.case': 'کیس',
    'hw.condition': 'وضعیت ظاهری',
    'hw.placeholder.cpu': 'مثال: Intel Core i7-13700K',
    'hw.placeholder.ram': 'مثال: 32GB DDR5 5600MHz',
    'hw.placeholder.gpu': 'مثال: NVIDIA RTX 4070',
    'hw.placeholder.storage': 'مثال: 1TB NVMe SSD',
    'hw.placeholder.motherboard': 'مثال: ASUS ROG Z790',
    'hw.placeholder.psu': 'مثال: 850W Gold',
    'hw.placeholder.case': 'مثال: NZXT H5 Flow',
    'hw.placeholder.condition': 'مثال: عالی، خوب، معمولی',
    'hw.placeholder.notes': 'هر یادداشت اضافی درباره این سیستم وارد کنید...',

    // All Systems
    'systems.title': 'همه سیستم‌ها',
    'systems.count': 'سیستم پیدا شد',
    'systems.no_results': 'سیستمی یافت نشد',
    'systems.adjust_filters': 'جستجو یا فیلترهای خود را تنظیم کنید',
    'systems.add_first': 'با افزودن اولین سیستم شروع کنید',
    'systems.search': 'جستجو بر اساس نام، شماره سریال یا سخت‌افزار...',
    'systems.all_categories': 'همه دسته‌بندی‌ها',
    'systems.all_statuses': 'همه وضعیت‌ها',
    'systems.filters': 'فیلترها',
    'systems.clear_filters': 'پاک کردن فیلترها',

    // System detail
    'detail.system_info': 'اطلاعات سیستم',
    'detail.hardware_specs': 'مشخصات سخت‌افزاری',
    'detail.notes': 'یادداشت‌ها',
    'detail.repair_history': 'تاریخچه تعمیرات',
    'detail.activity_log': 'گزارش فعالیت‌ها',
    'detail.quick_actions': 'اقدامات سریع',
    'detail.create_repair': 'ایجاد گزارش تعمیر',
    'detail.repair_tip': 'یک تیکت تعمیر جدید شروع کنید',
    'detail.entry_date': 'تاریخ ورود',
    'detail.created': 'ایجاد شده',
    'detail.last_updated': 'آخرین به‌روزرسانی',
    'detail.repairs': 'تعمیرات',
    'detail.activities': 'فعالیت‌ها',
    'detail.customer': 'مشتری',
    'detail.not_found': 'سیستم یافت نشد',
    'detail.confirm_delete': 'آیا مطمئن هستید؟ این عمل قابل بازگشت نیست.',
    'detail.delete_success': 'سیستم حذف شد',

    // Repair
    'repair.title': 'مرکز تعمیرات',
    'repair.count': 'گزارش تعمیر',
    'repair.new_record': 'گزارش تعمیر جدید',
    'repair.create': 'ایجاد گزارش تعمیر',
    'repair.edit': 'ویرایش گزارش',
    'repair.save': 'ذخیره تغییرات',
    'repair.cancel': 'انصراف',
    'repair.no_records': 'هیچ گزارش تعمیری یافت نشد',
    'repair.select_device': 'انتخاب دستگاه *',
    'repair.choose_device': 'یک دستگاه انتخاب کنید...',
    'repair.issue_desc': 'توضیحات مشکل',
    'repair.symptoms': 'علائم مشاهده شده',
    'repair.probable_cause': 'علت احتمالی',
    'repair.technician': 'تکنسین مسئول',
    'repair.status': 'وضعیت تعمیر',
    'repair.cost': 'هزینه تعمیر (تومان)',
    'repair.expected_completion': 'تاریخ اتمام مورد انتظار',
    'repair.completion_date': 'تاریخ تکمیل',
    'repair.create_success': 'گزارش تعمیر با موفقیت ایجاد شد',
    'repair.update_success': 'گزارش تعمیر به‌روزرسانی شد',

    // Repair detail
    'repair.detail.title': 'گزارش تعمیر',
    'repair.detail.details': 'جزئیات تعمیر',
    'repair.detail.assignment': 'تکلیف و هزینه',
    'repair.detail.timeline': 'زمان‌بندی',
    'repair.detail.technician': 'تکنسین مسئول',
    'repair.detail.not_assigned': 'تعیین نشده',
    'repair.detail.cost': 'هزینه تعمیر',
    'repair.detail.entry': 'تاریخ ثبت',
    'repair.detail.expected': 'تاریخ اتمام مورد انتظار',
    'repair.detail.completed': 'تاریخ تکمیل',
    'repair.detail.no_details': 'هنوز جزئیات تعمیری ثبت نشده است.',
    'repair.detail.not_found': 'گزارش تعمیر یافت نشد',

    // Repair detail sections
    'repair_field.probable_cause': 'علت احتمالی خرابی',
    'repair_field.issue_description': 'توضیحات مشکل',
    'repair_field.symptoms': 'علائم مشاهده شده',
    'repair_field.diagnostic_notes': 'یادداشت‌های تشخیصی',
    'repair_field.checked_parts': 'قطعات بررسی شده',
    'repair_field.replaced_parts': 'قطعات تعویض شده',
    'repair_field.repair_actions': 'اقدامات تعمیر انجام شده',
    'repair_field.tests_performed': 'تست‌های انجام شده',
    'repair_field.test_results': 'نتایج تست',
    'repair_field.technician_notes': 'یادداشت‌های تکنسین',

    // Customer systems
    'customer.title': 'سیستم‌های مشتری',
    'customer.no_results': 'سیستم مشتری وجود ندارد',
    'customer.desc': 'سیستم‌های متعلق به مشتریان در اینجا نمایش داده می‌شوند',

    // For sale
    'forsale.title': 'سیستم‌های برای فروش',
    'forsale.no_results': 'سیستمی برای فروش وجود ندارد',

    // Internal
    'internal.title': 'سیستم‌های داخلی',
    'internal.all': 'همه سیستم‌های داخلی',
    'internal.no_results': 'سیستم داخلی وجود ندارد',

    // Settings
    'settings.title': 'تنظیمات',
    'settings.subtitle': 'مدیریت تنظیمات کارگاه',
    'settings.appearance': 'ظاهر',
    'settings.system': 'سیستم',
    'settings.about': 'درباره',
    'settings.theme': 'حالت نمایش',
    'settings.light': 'روشن',
    'settings.dark': 'تاریک',
    'settings.current_theme': 'فعلی: {theme}',
    'settings.database': 'پایگاه داده',
    'settings.db_desc': 'SQLite (محلی)',
    'settings.application': 'برنامه',
    'settings.app_desc': 'مدیریت دستگاه‌ها نسخه ۱.۰.۰',
    'settings.stack': 'ساخته شده با Flask · SQLite · Tailwind CSS',
    'settings.design': 'طراحی شده برای فروشگاه‌های کامپیوتر، مراکز تعمیر و کارگاه‌های فنی',

    // Language
    'lang.en': 'English',
    'lang.fa': 'فارسی',
    'lang.switch': 'EN/FA',

    // Common
    'common.loading': 'در حال بارگذاری...',
    'common.failed': 'خطا در بارگذاری اطلاعات',
    'common.no_data': 'اطلاعاتی وجود ندارد',
    'common.save': 'ذخیره',
    'common.delete': 'حذف',
    'common.edit': 'ویرایش',
    'common.new': 'جدید',
    'common.back': 'بازگشت',
    'common.confirm': 'تأیید',
    'common.search': 'جستجو',
    'common.s_n': 'شماره سریال',
    'common.repairs': 'تعمیر',
    'common.no_repairs': 'بدون تعمیر',
    'common.tech': 'تکنسین',
    'common.cost': 'هزینه',

    // Repair actions log
    'repair.log_action': 'ثبت فعالیت',
    'repair.log_placeholder': 'فعالیت انجام شده را تایپ کنید...',

    // Toast messages
    'toast.system_created': 'سیستم با موفقیت ثبت شد!',
    'toast.system_deleted': 'سیستم حذف شد',
    'toast.status_updated': 'وضعیت به‌روزرسانی شد',
    'toast.repair_created': 'گزارش تعمیر با موفقیت ایجاد شد',
    'toast.repair_updated': 'گزارش تعمیر به‌روزرسانی شد',
    'toast.failed': 'عملیات ناموفق بود',
    'toast.select_device': 'لطفاً یک دستگاه انتخاب کنید',
  }
};

// ---- i18n Engine ----

let currentLang = localStorage.getItem('lang') || 'en';

function __(key) {
  const dict = translations[currentLang];
  if (!dict) return key;
  return dict[key] !== undefined ? dict[key] : key;
}

function setLanguage(lang) {
  if (!translations[lang]) return;
  currentLang = lang;
  localStorage.setItem('lang', lang);
  document.documentElement.setAttribute('lang', lang === 'fa' ? 'fa' : 'en');
  document.documentElement.setAttribute('dir', lang === 'fa' ? 'rtl' : 'ltr');
  if (lang === 'fa') {
    document.body.classList.add('rtl');
  } else {
    document.body.classList.remove('rtl');
  }
  translateDOM();
  renderSidebar();
  document.querySelectorAll('[data-i18n-render]').forEach(el => {
    try {
      const fn = window[el.getAttribute('data-i18n-render')];
      if (typeof fn === 'function') fn();
    } catch(e) {}
  });
  const toggle = document.getElementById('langToggle');
  if (toggle) toggle.textContent = __(lang === 'fa' ? 'lang.en' : 'lang.fa');
}

function toggleLanguage() {
  setLanguage(currentLang === 'en' ? 'fa' : 'en');
}

function translateDOM() {
  // data-i18n elements
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    const translated = __(key);
    if (translated && translated !== key) {
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' || el.tagName === 'SELECT') {
        if (el.hasAttribute('placeholder')) {
          el.setAttribute('placeholder', translated);
        }
      } else {
        el.textContent = translated;
      }
    }
  });
  // data-i18n-placeholder
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    el.setAttribute('placeholder', __(el.getAttribute('data-i18n-placeholder')));
  });
  // data-i18n-value (for input values)
  document.querySelectorAll('[data-i18n-value]').forEach(el => {
    el.value = __(el.getAttribute('data-i18n-value'));
  });
  // data-i18n-title
  document.querySelectorAll('[data-i18n-title]').forEach(el => {
    el.setAttribute('title', __(el.getAttribute('data-i18n-title')));
  });
}

// Override helper functions for status/category badges to use translations
function tStatusLabel(status) {
  return __(`status.${status}`) || status;
}

function tRepairStatusLabel(status) {
  return __(`repair_status.${status}`) || status;
}

function tCategoryLabel(cat) {
  return __(`category.${cat}`) || cat;
}

// Persian date formatter
function formatDate(d) {
  if (!d) return '—';
  try {
    if (currentLang === 'fa') {
      return new Date(d).toLocaleDateString('fa-IR', { year: 'numeric', month: 'long', day: 'numeric' });
    }
    return new Date(d).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
  } catch(e) {
    return d;
  }
}

function formatDateTime(d) {
  if (!d) return '—';
  try {
    if (currentLang === 'fa') {
      return new Date(d).toLocaleDateString('fa-IR', { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' });
    }
    return new Date(d).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
  } catch(e) {
    return d;
  }
}

// Override statusBadge and categoryBadge to use translations
const _origStatusColors = {
  'READY': 'bg-emerald-100 text-emerald-700 border-emerald-300',
  'IN_REPAIR': 'bg-amber-100 text-amber-700 border-amber-300',
  'DAMAGED': 'bg-red-100 text-red-700 border-red-300',
  'DELIVERED': 'bg-blue-100 text-blue-700 border-blue-300',
  'SOLD': 'bg-purple-100 text-purple-700 border-purple-300',
  'PENDING_INSPECTION': 'bg-orange-100 text-orange-700 border-orange-300',
  'TESTED': 'bg-teal-100 text-teal-700 border-teal-300',
  'ARCHIVED': 'bg-gray-100 text-gray-700 border-gray-300',
  'PENDING': 'bg-orange-100 text-orange-700 border-orange-300',
  'IN_PROGRESS': 'bg-amber-100 text-amber-700 border-amber-300',
  'COMPLETED': 'bg-emerald-100 text-emerald-700 border-emerald-300',
  'CANCELLED': 'bg-gray-100 text-gray-700 border-gray-300',
};
const _origCategoryColors = { 'CUSTOMER': 'bg-sky-100 text-sky-700 border-sky-300', 'FOR_SALE': 'bg-violet-100 text-violet-700 border-violet-300', 'INTERNAL': 'bg-rose-100 text-rose-700 border-rose-300' };

function statusBadge(status) {
  const color = _origStatusColors[status] || 'bg-gray-100 text-gray-700 border-gray-300';
  const label = tStatusLabel(status);
  return `<span class="badge ${color}">${label}</span>`;
}

function categoryBadge(cat) {
  const color = _origCategoryColors[cat] || 'bg-gray-100 text-gray-700 border-gray-300';
  const label = tCategoryLabel(cat);
  return `<span class="badge ${color}">${label}</span>`;
}

// Hardware datalist helper
function renderHardwareDatalists() {
  fetch('/api/hardware').then(r => r.json()).then(catalog => {
    Object.entries(catalog).forEach(([type, items]) => {
      const existing = document.getElementById('hw-' + type + '-list');
      if (existing) existing.remove();
      const datalist = document.createElement('datalist');
      datalist.id = 'hw-' + type + '-list';
      items.forEach(item => {
        const opt = document.createElement('option');
        opt.value = item;
        datalist.appendChild(opt);
      });
      document.body.appendChild(datalist);
    });
  });
}

// Override showToast to use i18n
const _origShowToast = window.showToast;
window.showToast = function(msg, type) {
  const t = document.getElementById('toastContainer');
  t.textContent = msg;
  t.className = 'toast show ' + (type === 'error' ? 'toast-error' : 'toast-success');
  setTimeout(() => t.classList.remove('show'), 3000);
};

// Init
document.addEventListener('DOMContentLoaded', () => {
  setLanguage(currentLang);
});
