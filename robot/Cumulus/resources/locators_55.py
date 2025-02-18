"""Locators for summer '22"""

npsp_lex_locators={
	'breadcrumb': "//li[contains(@class, 'slds-breadcrumb__item')]/span[text()='{}']",
	'spl-breadcrumb':"//div[@class= 'slds-media__body']/p[text()='{}']",
	'breadcrumb-link':"//a[@title='{}' and contains(@class,'BreadCrumbItem')]",
	'obj-header':"//h1//*[text()='{}']",
	'button-title':"//button[@title='{}']",
	'button-text':'//button[text()="{}"]',
	'button-with-text':'//button[contains(text(),"{}")]',
	'dropdown_spinner': 'css: div#divLoading',
	'placeholder': "//*[contains(@placeholder,'{}')]",
	'datatable':"//*[contains(@data-qa-locator,'{}')]//tbody/tr[./th//*[text()='{}']]/td[@data-label='{}']",
	'app_launcher':{
		'select-option':'//span/mark[text()="{}"]',
	},
	'object_dd':'//div[contains(@class,"slds-dropdown-trigger slds-dropdown-trigger_click")]//button/lightning-icon',
	'main-header':{
		"header_text": "//h1/div/span",
		"header_text_spl": "//h1//lightning-formatted-text",
	},
	"record": {
		'button':"//lightning-button/button[.='{}']",
		'select_value':"//li/a[text()='{}']",
		'select_dropdown':"//a[@class='select']",
		'footer':"//div[@class='footer active' or contains(@class,'footer-visible')]",
		'ltdatepicker':"//td[not(contains(@class,'slds-disabled-text'))]/*[text()='{}']",
		'lt_date_picker':"//label[./*[text()='{}']]/following-sibling::div//*[contains(@class,'input')]",
		'month_pick':"//div[@class='dateBar']//a[@title='{}']",
		'activity-button':'//button[contains(@class,"{}")]',
		'dd_edit_option': '//div[contains(@class,"branding-actions")]/ul/li/a[@title="{}"]',
		'edit_button':'//*[@title="{}"]',
		'edit_form': 'css: div.forcePageBlockItemEdit',
		'flexipage_edit_form': 'css: force-record-layout-item.slds-is-editing',
		'list':"//div[contains(@class,'forcePageBlockSectionRow')]/div[contains(@class,'forcePageBlockItem')]/div[contains(@class,'slds-hint-parent')]/div[@class='slds-form-element__control']/div[.//span[text()='{}']][//div[contains(@class,'uiMenu')]//a[@class='select']]",
		'rdlist':"//label[text()='{}']/following-sibling::div//div[contains(@class,'slds-dropdown-trigger') and @role='combobox']",
		'flexipage-list':'//lightning-combobox[./label[text()="{}"]]//input[contains(@class,"combobox__input")]',
		'dropdown':"//div[@class='select-options']/ul[@class='scrollable']/li[@class='uiMenuItem uiRadioMenuItem']/a[contains(text(),'{}')]",
		'related': {
			'button':"//article[contains(@class, 'slds-card slds-card_boundary')][.//img][.//span[@title='{}']]//*[text()='{}']",
			'check_occurrence':'//h2/a/span[@title="{}"]/following-sibling::span[@title="{}"]',
			'drop-down':'//div[contains(@class, "slds-card")]/header[.//span[@title="{}"]]/parent::*/div/div/div/a[contains(@class, "slds-button")]',
			'title':'//div/h2//a[./span[text()="{}"]]',
			'viewall':'//article[contains(@class, "slds-card slds-card_boundary")][.//span[@title="{}"]]//a[.//span[@class="view-all-label"]]',
			'item':"//article[contains(@class, 'slds-card_boundary')][.//img][.//span[@title='{}']]//h3//a",
			'field_value': '//a[text()="{}"]/ancestor::li//div[contains(@class, "slds-item--detail")]//*[text()="{}"]',
			'link':"//article[contains(@class, 'slds-card slds-card_boundary')][.//span[@title='{}']]//table/tbody/tr[.//td//*[text()='{}']]/th//a",
			'dd-link':'//a[@name="{}"]',
			'allocations':"//article[contains(@class, 'slds-card slds-card_boundary')][.//table[@aria-label='{}']]//tbody/tr[.//td//*[text()='{}']]/td//*[text()='{}']",
			"popup_trigger": "//article[.//span[@title='{}']]//tr[.//*[text()='{}']]//div[contains(@class,'slds-truncate')]//button[./span[text()='Show Actions']]",
		},
	},
	"popup-link":"//div[contains(@class, 'uiPopupTarget')][contains(@class, 'visible')]//a[@title='{}']",
	"alert": "//span[contains(@class,'toastMessage')]/a/div",
	"alert-text":"//span[contains(@class,'toastMessage')]",
	'batch_status':'//div[contains(@class,"slds-tile__title")][.//*[text()="{}"]]/div[contains(@class,"slds-col")]//span[text()="{}"]',
	'popup': "//div[contains(@class, 'uiPopupTarget')][contains(@class, 'visible')]",
	'flexipage-popup':"//div[contains(@class, 'slds-is-open')][contains(@class, 'slds-combobox')]",
	'newflexi-popup':"//div[contains(@class,'modal-body')]//*[contains(@class,'slds-combobox')]",
	'test':'/html/body/div[6]/table/tbody/tr[23]/td[1]/a',
	"toast-msg":"//span[@class='toastMessage slds-text-heading--small forceActionsText']",
	"toast-close":"//button[contains(@class,'toastClose')]",
	'frame_new':'//iframe[contains(@name, "{}") or contains(@title, "{}")]',
	'frame':'//iframe[@title= "{}"]',
	'frame_by_name': "//iframe[contains(@name, '${}')]",
	'id':'//*[contains(@id,"{}")]',
	'button':'//input[contains(@value,"{}")]',
	'link':'//a[.//span[text()="{}" or contains(text(),"{}")]]',
	'more_actions_link':"//button[contains(@class,'slds-button_icon-border-filled') and @aria-haspopup='true']",
	'link-text':'//a[contains(text(),"{}")]',
	'link-title':'//a[@title="{}"]',
	'lightning-button':'//lightning-button/button[contains(text(),"{}")]',
	'link-contains':'//button[.//span[contains(text(),"{}")]]',
	'label':'//label[text()="{}"]',
	'checkbox':{
		'model-checkbox':'//div[contains(@class,"uiInputCheckbox")]/label/span[text()="{}"]/../following-sibling::input[@type="checkbox"]',
		'details-checkbox':'//label[@class="slds-checkbox__label"][./span[text()="{}"]]/following-sibling::div//input',
		'table_checkbox':'//tbody/tr[./td[2]/a[text()="{}"]]/td/input[@type="checkbox"]',
		'id':'//input[@type="checkbox" and contains(@id,"{}")]',
	},
	'tabs':{
		'tab': "//div[@class='uiTabBar']/ul[@class='tabs__nav']/li[contains(@class,'uiTabItem')]/a[@class='tabHeader']/span[contains(text(), '{}')]",
		'spl-tab':"//div[@class='slds-tabs_default']//ul[@class='slds-tabs_default__nav']/li[contains(@class,'slds-tabs_default__item')]/a[text()= '{}']",
	},
	'desktop_rendered': 'css: div.desktop.container.oneOne.oneAppLayoutHost[data-aura-rendered-by]',
	'loading_box': 'css: div.auraLoadingBox.oneLoadingBox',
	'contacts_actions_dropdown_menu': 'css: a.slds-grid--align-center[aria-expanded="true"]',
	'household_lookup_dropdown_menu': 'css: div.slds-show',
	'spinner': 'css: div.slds-spinner',
	'Delete_opportunity_modal_button': 'css: div.forceModalActionContainer button.uiButton--brand',
	'modal_field':"//div[contains(@class, 'lookupInput')][./label[contains(text(), '{}')]]/div//span[@class='lookupInput']/input",
	'name':'//tbody/tr/th/span/a',
	'select_name':'//tbody//a[text()= "{}"]',
	'opportunities_dropdown':"css:a.slds-button.slds-button--icon-border-filled",
	'locate_dropdown':'//tbody/tr[{}]/td/span//div/a',
	'locating_delete_dropdown':'//tbody//a[text()= "{}"]/../../following-sibling::td/span//div/a/lightning-icon',
	'related_name':'//tbody/tr/td/a[contains(@class,"forceOutputLookup")]',
	'rel_loc_dd':'//tbody/tr[{}]/td[4]//lightning-primitive-icon',
	'delete_icon':'//*[contains(@class,"slds-form-element")][./label[text()="{}"]]//input[@placeholder="{}"]/following-sibling::div/button',
	'delete_icon_record':'//label[contains(text() ,"{}")]/following::input[@placeholder = "{}"]/following-sibling::div/child::button[@title="Clear Selection"]',
	'aff_list':'//div[@role="tablist"]/following::div[@class = "container forceRelatedListSingleContainer"][7]/article/div[@class="slds-card__body"]/div/div/div/div/div/div/div/table/tbody/tr/td[1]',
	'aff_status':'//table[contains(@class,"slds-table")]/tbody/tr[./td//a[text()="{}"]]/td[@data-label="Relationship Explanation"]',
	'relationship_status':'//lightning-formatted-text[contains(text(),"is")]',
	'aff_id':'//table[contains(@class,"slds-table")]/tbody/tr[./td//a[text()="{}"]]/th//a',
	'click_aff_id':'//table[contains(@class,"forceRecordLayout")]/tbody/tr/th/div/a[text()="{}"]',
	'confirm': {
		'check_value':'//div[contains(@class, "forcePageBlockItem") or contains(@class, "slds-form-element_stacked")][.//span[text()="{}"]]//following-sibling::div[.//span[contains(@class, "test-id__field-value")]]//*[text()="{}"]',
		'check_text_value':'//div[contains(@class, "field-label-container")][.//span[text()="{}"]]//following-sibling::div[.//span[contains(@class, "test-id__field-value")]]/span//lightning-formatted-text',
		'check_status':'//div[contains(@class, "field-label-container")][.//span[text()="{}"]]//following-sibling::div[.//span[contains(@class, "test-id__field-value")]]/span//lightning-formatted-text[text()="{}"]',
		'check_numbers':'//div[contains(@class, "field-label-container")][.//span[text()="{}"]]//following-sibling::div[.//span[contains(@class, "test-id__field-value")]]/span//lightning-formatted-number[text()="{}"]',
	},
	'check_field':'//div[contains(@class, "forcePageBlockItem")][.//span[text()="{}"]]//following-sibling::div[.//span[contains(@class, "test-id__field-value")]]/span/div//a',
	'check_field_spl':'//div[contains(@class, "field-label-container")][.//span[text()="{}"]]//following-sibling::div[.//span[contains(@class, "test-id__field-value")]]//a',
	'account_list':'//tbody/tr/th[.//span[contains(@class, "slds-grid")]]/descendant::a[text()="{}"]',
	'dd_options':'//*[@id="p3"]/option[text()="{}"]',
	'related_list_items':'//article[contains(@class,"slds-card_boundary")][.//a[contains(@class, "slds-card")]/span[text() = "{}"]]//div[contains(@class, "listDisplays")]//*[text()="{}"]',
	'span_button':'//span[text()="{}"]',
	'modalspan_button':'//div[contains(@class,"modal-body")]//span[text()="{}"]',
	'related_drop_down':'//div/a[contains(@class,"slds-button")]/ancestor::li/div/a',
	'span':"//span[@title='{}']",
	'header_field_value':'//*[contains(@class, "slds-page-header__detail")][.//*[@title="{}"]]//*[text()="{}"]',
	'header_datepicker':'//li[contains(@class, "slds-page-header__detail")][.//p[contains(@class, "slds-text-heading--label")][@title="{}"]]//*[@class="uiOutputDate"]',
	'select_one_record':"//tbody/tr[1]/th/span/a",
	'click_search':'//div[@class="slds-form-element"][./label[text()="{}"]]/div/span/span/input[contains(@id,"inputX")]',
	'field': "//div[contains(@class, 'uiInput')][.//label[contains(@class, 'uiLabel')][.//span[text()='{}']]]//input",
	'field_lookup_value': "//a[@role='option'][.//div[@title='{}']]",
	'field-value':"//div[contains(@class,'slds-form-element')][./label[text()='{}']]/div/span",
	'header':'//h1//child::div/span[text()="{}"]',
	'check_related_list_item':'//article[.//span[text() = "{}"]]/descendant::tbody//th/*/*/*/*/*/*/*/*/a/span[text()="{}"]',
	'detail_page': {
		'section_header':'//h3//span[text()="{}"]',
		'address':'//h3[contains(@class, "slds-section__title")][.//span[contains(text(),"Address")]]/../..//div[contains(@class, "test-id")]/span[text()= "{}"]/../following-sibling::div//a//div[contains(@class, "slds")]',
		'field':'//h3[contains(@class, "slds-section__title")][.//span[text()="{}"]]/../..//div[contains(@class, "test-id")]/span[text()= "{}"]/../following-sibling::div//span[text()="{}"]',
		'field-value':{
			'verify_field_value1':'//div[contains(@class, "forcePageBlockItem")]/div/div//span[text()="{}"]/../../div[2]/span/span[text() = "{}"]',
			'verify_field_value2':'//force-record-layout-item//div[./span[text()="{}"]]/following-sibling::div//lightning-formatted-text[text() = "{}"]',
		},
		'edit_mode':{
			'section_header':'//div[contains(@class,"forcePageBlockSectionEdit")]/h3//span[text()="{}"]',
		},
	},
	
	'manage_hh_page':{
		'address_link':'//h4[text()="{}"]',
		'address':'//div[contains(@class, "uiInput")][.//label[contains(@class, "uiLabel")]/span[text()="{}"]]/',
		'mhh_checkbox':'//*[@id="SortCanvas"]/li//a[text()="{}"]/ancestor::div[contains(@class, "slds-card__header")]/following-sibling::div[contains(@class,"slds-card__body")]//form//div//label/span[@id = "{}"]',
		'button':'//*[text()="{}"]',
		'more_actions_btn': "//lightning-button-menu/button",
		'add_contact_option':'//li/span[text()="{}"]',
		'lookup':'//div[./span[text()="{}"]]//input',
	},
	'opportunity':{
		'contact_role':'//div[contains(@class,"listItemBody")][./h3//a[text()="{}"]]//parent::h3/following-sibling::ul/li/div[contains(@class,"forceListRecordItem")]/div[@title="Role:"]/following-sibling::div/span[text()="{}"]',
	},
	'object':{
		'record':'//tbody//a[text()= "{}"]',
		'field':"//lightning-textarea[.//label[text()='{}']]//textarea",
		'button': "//div[contains(@class,'windowViewMode')]//ul[contains(@class,'forceActionsContainer')][contains(@class,'oneActionsRibbon')]//a[@title='{}']",
		'radio_button':"//div[contains(@class,'changeRecordTypeRightColumn')]/div/label[@class='slds-radio']/div[.//span[text()='{}']]/preceding::div[1]/span[@class='slds-radio--faux']",
		'field-value':'//tbody/tr[./th//a[text()="{}"]]/td[.//span[text()="{}"]]',
	},
	'engagement_plan':{
		'input_box':'//fieldset[./legend[text()="{}"]]//div[@class="requiredInput"]/input',
		'dropdown':'//div[contains(@class,"slds-p-top_small")]/label[text()="{}"]/following-sibling::div/select',
		'checkbox':'//div[contains(@class,"slds-p-top_small")]/label[@class="slds-checkbox"][./span/following-sibling::{}[text()="{}"]/]',
		'button':'//div[contains(@class,"slds-button-group")][.//span[text()="toTask {}"]]/button[contains(text(),"{}")]',
		'check_eng_plan':'//h2/a/span[@title="{}"]//ancestor::div[contains(@class, "slds-card__header slds-grid")]/following-sibling::div//tbody/tr/th/div/a',
		'dd':'//h2/a/span[@title="{}"]//ancestor::div[contains(@class,"slds-card__header slds-grid")]/following-sibling::div//tbody/tr/th/div/a/ancestor::th/following-sibling::td//lightning-primitive-icon',
		'tasks':'//div[contains(@class,"slds-section__content")]/ul/li//a[text()="{}"]',
	},
	'levels':{
		'id':'//input[contains(@id,"{}")]',
		'select':'//select[contains(@id,"{}")]',
		
	},
	'custom_objects':{
		'actions-link':'//a[@title="{}" or @name="{}"]',
		'option':'//a/span[text()="{}"]'
	},
	'payments':{
		'date_loc':"//*[@id='pmtTable']/tbody/tr/td[3]/div//input",
		'no_payments':'//tbody/tr[./th//a[contains(@title,"PMT")]]/td[2]',
		'pays':'//tbody/tr[./th//a[contains(@title,"PMT")]]/td[.//span[text()="{}"]]',
		'pay_amount':'//tbody/tr[{}]/td[3]/span/span[text()="{}"]',
		'check_occurrence':'//h2/a/span[@title="{}"]/following-sibling::span',
		'text':'//*[@id="j_id0:vfForm:j_id76:util_formfield:inputx:util_inputfield:inputX"]',
		'field-value':"//div[contains(@class,'slds-form-element')][./span[text()='{}']]/following-sibling::div",
		'allocations':"//article[contains(@class, 'slds-card slds-card_boundary')][.//span[@title='{}']]//tbody/tr[./td//a[text()='{}']]/th",
		'loc1':"//tbody/tr/td[2]/span/span",
		'loc2':"//tbody/tr/td[3]/span/span",
	},
	'gaus':{
		'input_field':'//div[@class="slds-form-element"][./label[text()="{}"]]/div/input',
	},
	'npsp_settings':{
		'main_menu':'//div[@class="slds-tree__branch slds-tree__item"][.//a[text()="{}"]]',
		'donations_link':'//div/a[contains(text(),"{}") and not(contains(text(),"Recurring Donations"))]',
		'main_menu_link':'//div/a[contains(text(),"{}")]',
		'panel_sub_link':'//ul/li[contains(@class,"slds-is-selected")]/a[text()="{}"]',
		'field_value':"//div[@class='slds-form-element'][./label[contains(text(),'{}')]]/div/span",
		'side_panel':'//div[@id="{}"]//child::button[contains(@class,"chevronright")]',
		'list':"//div[@class='slds-form-element']/label[text()='{}']/following-sibling::div/select",
		'multi_list':'//div[contains(@class,"slds-form_horizontal")]/div[@class="slds-form-element"][./label[text()="{}"]]/div//select',
		'list_val':'//div[@class="slds-form-element"]/label[text()="{}"]/following-sibling::div/span[text()="{}"]',
		'status':'//div[contains(@class,"slds-tile__title")][.//span[text()="{}"]]/div[contains(@class,"slds-col")]//span[text()="{}"]',
		'button':'//form[.//h1[contains(text(),"{}")]]//input[contains(@value,"{}")]',
		'completed':'//span[contains(@class, \'slds-theme_success\')]',
		'batch-button':'//div[@id="{}"]//child::input[@value="{}"]',
		'checkbox':'//label[./span[text()="{}"]]/descendant::span[@class="slds-checkbox_faux"]',
		'erd_status_mapping_header':"//div/h1[contains(text(),'{}')]",
		'erd_state_status_mapping':"//tr[@data-row-key-value='{}']//lightning-primitive-cell-factory[@data-label='State']//lightning-base-formatted-text",
		'table_dropdown':"//tbody/tr[./th//*[text()='{}']]/td//button",
		'page_error':'//div[.//span[text()="{}"]]/slot//li[text()="{}"]',
		'field_error':'//tr[./td[@data-label="Field API Name"]//*[text()="{}"]]/td//button[contains(@class,"error")]'
	},
	'data_imports':{
		'status':'//div[contains(@class,"slds-tile__title")][./p[text()="BDI_DataImport_BATCH"]]/div[contains(@class,"slds-col")]/span[text()="{}"]',
		'checkbox':'//tr[./th//a[@title="{}"]]/td//span[@class="slds-checkbox--faux"]',
		'actions_dd':'//button[@aria-expanded="true"][.//span[contains(text(),"more actions")]]',
		'check_status':'//div[contains(@class, "field-label-container")][.//span[text()="{}"]]//following-sibling::div[.//span[contains(@class, "test-id__field-value")]]/span//lightning-formatted-text',
	},
	'bge':{
		'checkbox':'//label/span[text()="{}"]//parent::label/span[@class="slds-checkbox_faux"]',
		'field-duellist':'//label[text()="{}"]/following-sibling::lightning-dual-listbox//div[contains(@class,"slds-dueling-list__column")][./span[text()="{}"]]//div[contains(@class,"slds-dueling-list__options")]/ul/li//span[text()="{}"]',
		'duellist':'//h3[./span[text()="{}"]]/following-sibling::div//div[contains(@class,"slds-dueling-list__column")][./span[text()="{}"]]//div[contains(@class,"slds-dueling-list__options")]/ul/li//span[text()="{}"]',
		'duellist2':'//div/div[text()="{}"]/following-sibling::div//div[contains(@class,"slds-dueling-list__column")][./span[text()="{}"]]//div[contains(@class,"slds-dueling-list__options")]/ul/li//span[text()="{}"]',
		'field-select-button':'//label[text()="{}"]/following-sibling::lightning-dual-listbox//div[contains(@class,"slds-dueling-list__column")]//button[@title="{}"]',
		'select-button':'//h3[./span[text()="{}"]]/following-sibling::div//div[contains(@class,"slds-dueling-list__column")]//button[@title="{}"]',
		'select-button2':'//div/div[text()="{}"]/following-sibling::div//div[contains(@class,"slds-dueling-list__column")]//button[@title="{}"]',
		'title':'//p[text()="{}"]/following-sibling::h1',
		'field-input':'//label[text()="{}"]/following-sibling::div/input',
		'field-text':'//label[text()="{}"]/following-sibling::div/textarea',
		'button':'//div[contains(@class,"active")]/descendant::button[text()="{}"]',
		'month':"//div[@class='slds-align-middle']//button[@title='{}']",
		'date':"//div[contains(@class,'slds-datepicker')]//table[@class='slds-datepicker__month']//span[text()='{}']",
		'card-header':'//article[./div[@class="slds-card__body"]//lightning-formatted-text[text()="{}"]]//header',
		'edit_button':'//td[@data-label="{}"]//button',
		'edit_field':'//lightning-primitive-datatable-iedit-panel//input',
		'count':'//div[contains(@class,"BGE_DataImportBatchEntry")]//tbody/tr',
		'value':'//td[@data-label="{}"]//a',
		'name':'//div[contains(@class,"BGE_DataImportBatchEntry")]//tbody/tr/th//a',
		'locate_dropdown':'//div[contains(@class,"BGE_DataImportBatchEntry")]//tbody/tr[{}]/td[6]//div//button[./span[text()="Show actions"]]/lightning-primitive-icon',
		'gift-amount':'//div[./label[text()="{}"]]',
		'modal-link':'//tbody/tr/td/a[text()="{}"]',
		'datepicker_open':"//div[contains(@class,'slds-is-open')][./label[contains(text(),'{}')]]",
	},
	'bge-lists':{
		'list1':"//div[./label[text()='{}']]/div//select",
		'list2':"//div[contains(@class,'slds-grid')]/div[contains(@class,'slds-text-align_left')]/span[text()='{}']/../following-sibling::div//select",
		'list3':"//div[./label/span[text()='{}']]/div//select",
		
	},
	'bge-duellist-btn':{
		'select-button':'//h3[./span[text()="{}"]]/following-sibling::div//div[contains(@class,"slds-dueling-list__column")]//button[@title="{}"]',
		'select-button2':'//div/div[text()="{}"]/following-sibling::div//div[contains(@class,"slds-dueling-list__column")]//button[@title="{}"]',
		'field-select-button':'//label[text()="{}"]/following-sibling::lightning-dual-listbox//div[contains(@class,"slds-dueling-list__column")]//button[@title="{}"]',
	},
	
	'object_manager':{
		'button':'//input[@title="{}"]',
		'input':'//input[@id="{}"]',
		'select_related':'//select[@id = "{}"]',
		'select_related_option':'//select[@id = "DomainEnumOrId"]/option[@value="{}"]',
		'search_result': '//tbody/tr/td/a/span[contains(text(),"{}")]',
		'formula_txtarea': '//textarea[@id = "{}"]',
		'object_result': '//th/a[text()="{}"]',
		'field_result': '//td/a/span[text()="{}"]',
		'new_picklist_btn': '//td[@class="pbButton"]/input[@title="{}"]',
		'picklist_txtarea': '//textarea[@title = "{}"]',
		'field_dropdown':'//tr[./td/a/span[text()="{}"]]/td//div[contains(@class,"slds-dropdown-trigger")]/a',
	},
	'custom_settings':{
		'subtree':'//a/mark[text()="{}"]',
		'link':"//table[@class='list']/tbody/tr[./th/a[text()='{}']]/td/a[text()='{}']",
		'cbx_status':'//table[@class="detailList"]/tbody/tr/th[./span[text()="{}"]]/following-sibling::td//img[@title="{}"]',
	},
	'adv_mappings':{
		'dropdown':"//tr[./th//*[text()='{}']]/td[.//span[text()='Show actions']]//button",
		'modal_open':'//div[contains(@class,"slds-backdrop_open")]',
		'field_mapping':'//input[@name="{}"]',
		'combobox':'//div[contains(@class,"slds-listbox") and @role="listbox"]',
		'footer-btn':"//footer[@class='slds-modal__footer']/button[text()='{}']",
		'field-label':'//lightning-primitive-cell-factory//*[text()="{}"]',
		'field_dd_option':'//div[contains(@class,"slds-input-has-icon")][./input[@name="{}"]]/following-sibling::div//span[@title="{}"]',
	},
	'modal-form':{
		'label':'//div[./*/*[text()="{}"]]',
	},
	# Customizable rollups related element locators
	'crlps':{
		'select_locator': "//select[@name ='{}']",
		'success_toast': "//div[@class='{}']",
		'active_setting_record': "//td[@data-label='Active']/following::tr/th//span/div//lightning-button/button[text()='{}']",
		'rollup_progress_notification': "//div/h2[contains(text(),'{}')]",
		'rollup_options':"//tr[./th//button[text()='{}']]/td//button",
		'modal-button': '//footer/button[text()="Save"]',
	},
	'gift_entry':{
		'id':'//*[contains(@data-qa-locator,"{}")]',
		'button':'//*[contains(@data-qa-locator,"{}")]/button',
		'field_input':'//*[contains(@data-qa-locator,"{}")]//child::{}',
		'field_span':'//*[contains(@data-qa-locator,"{}")]//child::span[text()="{}"]',
		'actions_dropdown':'//tbody/tr[./th//a[text()="{}"]]/td//button',
		'form_object_dropdown':'//*[@data-qa-locator="{}"]//button',
		'object_field_checkbox':'//*[@data-object-mapping-label="{}" and contains(@data-qa-locator,"{}")]//child::input',
		'field_alert':"//*[contains(@data-qa-locator,'{}')]/div[@role='alert' and text()='{}']",
		'count':'//lightning-layout[.//span[text()="{}"]]//child::lightning-layout-item//strong[text()="{}"]',
		'duellist':'//div[contains(@class,"slds-dueling-list__column")][./span[text()="{}"]]//div[contains(@class,"slds-dueling-list__options")]/ul/li//span[text()="{}"]',
		'table':'//*[@data-qa-locator="datatable {}"]//tbody//lightning-primitive-cell-factory[@data-label="{}"][.//*[text()="{}"]]',
		'lookup-option':'//li/lightning-base-combobox-item[.//*[@title="{}"]]',
		'datatable_options_icon':"//*/lightning-primitive-cell-factory/span/div//a[contains(text(),'{}')]/following::lightning-primitive-cell-actions//button[@aria-expanded='false']/lightning-primitive-icon",
		'datatable_field_by_name':"//lightning-primitive-cell-factory/span/div//a[contains(text(),'{}')]/following::lightning-primitive-cell-factory[@data-label='{}'][.//*[text()='{}']]",
		'datatable-menu-item':"//lightning-menu-item/a/span[text()='{}']",
		'new-section-field-bundle':"//article[@data-qa-locator='form section New Section'][.//label[text()='{}']]",
		'alert':'//div[@role="alert" and contains(@class,"slds-theme_{}")][./span[text()="{}"]]/h2[text()="{}"]',
		'element_text':'//*[contains(@data-qa-locator,"{}") and text()="{}"]',
		'page_error':'//div[contains(@class,"pageLevelErrors")]',
		'picklist_values':'//*[contains(@data-qa-locator,"{}")]//child::lightning-base-combobox-item[@data-value="{}"]',
		'modal_field':'//div[@class="modal-body scrollable slds-modal__content slds-p-around--medium"]//*[contains(@data-qa-locator,"{}")]//child::{}',
		'modal_button':'//div[@class="modal-body scrollable slds-modal__content slds-p-around--medium"]//*[contains(@data-qa-locator,"{}")]/button',
		'modal_id':'//div[@class="modal-body scrollable slds-modal__content slds-p-around--medium"]//*[contains(@data-qa-locator,"{}")]',
		'modallookup-option':'//div[@class="modal-body scrollable slds-modal__content slds-p-around--medium"]//li/lightning-base-combobox-item[.//*[@title="{}"]]',
		'remove_lookup':'//div[@class="modal-body scrollable slds-modal__content slds-p-around--medium"]//*[contains(@data-qa-locator,"button Remove selected option Opportunity: Record Type")]',
		'click-dropkown-value':"//div[@class='modal-body scrollable slds-modal__content slds-p-around--medium']//*[contains(@class,'slds-combobox')]//span[text()='{}'']",
		'modal_lookup_button':'//div[contains(@class,"modal-body")]//*[contains(@data-qa-locator,"{}")]//child::button',
		'form_error':'//div[.//span[text()="{}"]]/div[text()="{}"]',
		'field_error':'//*[contains(@data-qa-locator,"{}")]/div[text()="{}"]',
		'temp_builder_labels':'//lightning-input[@class="slds-truncate slds-form-element"]//label',
		'ge_form_labels':'//label[@class="slds-form-element__label" or @class="slds-form-element__label slds-no-flex"]',
		'temp_builder_sections':'//h2[@class="slds-card__header-title"]',
		'ge_form_sections':'//span[contains(@title,"{}")]',
		'progress_bar':'//lightning-layout-item[.//span[text()="{}"]]//child::lightning-layout-item//*[text()="{}"]',
		'batch_error':'//div[@role="alert" and contains(@class,"slds-theme--error")]//div[text()="{}"]/following-sibling::span[text()="{}"]',
		'close_error':'//div[@role="alert" and contains(@class,"slds-theme--error")]//child::button',
		'perms_error':'//div[@class="slds-illustration slds-illustration_large"]',
		'template_required_checkbox':'//lightning-input[@data-qa-locator="checkbox Required {}"]',
		'success_toast':'//span[contains(text(),"{} was processed.")]',
        'collapse_header':'//span[contains(@title,"Gift Entry Form")]',
		'form_header':'//span[contains(text(),"{}")]'
	},
	# Enhanced Recurring Donation (erd) related element locators
	'erd':{
		'active_schedules_card': "//div[contains(@class, 'slds-media__body')]/h3[contains(@title,'{}')]",
		'modal_dropdown_selector': "//label[text()='{}']/following-sibling::div//div[contains(@class,'slds-dropdown-trigger')]",
		'modal_input_field': "//label[text()='{}']/following-sibling::div/input",
		'modal_selection_value': "//lightning-base-combobox-item[@data-value='{}']",
		'installment_row' : "//table[contains(@class, 'slds-table_edit')]/tbody/tr",
		'text_message':'//span[contains(@class,"slds-text-color_error")]',
		'rd2_installed': "//c-progress-ring/following-sibling::lightning-formatted-text[text() = 'Enable Enhanced Recurring Donations']",
		'installment_date' : "//table[contains(@class, 'slds-table_edit')]/tbody/tr[{}]/th//span/div/lightning-formatted-date-time",
		'formatted_number':"//lightning-formatted-text[text() = '{}']/following::lightning-layout-item[contains(@class,'slds-dl_horizontal__detail')]/slot/lightning-formatted-number",
		'formatted_date':"//lightning-formatted-text[contains(text(),'{}')]/following::lightning-layout-item[contains(@class,'slds-dl_horizontal__detail')]/slot/lightning-formatted-date-time",
		'formatted_text':"//lightning-formatted-text[contains(text(),'{}')]/following::lightning-layout-item[contains(@class,'slds-dl_horizontal__detail')]/slot/lightning-formatted-text",
		'pause_date_checkbox':"//h2[contains(text(),'Pause')]/following::th//span/div/lightning-formatted-date-time[text()='{}']/ancestor::tr/td/descendant::label/span[contains(@class,'checkbox')]",
		'date_with_paused_txt':"//td//lightning-base-formatted-text[text()='Paused']/preceding::th//lightning-formatted-date-time[text()='{}']",
		'warning_message':'//lightning-formatted-rich-text/span[contains(text() ,"{}")]'
	},
	
}

extra_locators={
	'related_list_items1':'//div[@class = "forceRelatedListContainer"][.//a[contains(@class, "slds-card")]]//span[text() = "Relationships"]/ancestor::div[contains(@class, "slds-card")]/following-sibling::div[contains(@class, "slds-card")]//tbody//td/span[text()="{}"]',
}