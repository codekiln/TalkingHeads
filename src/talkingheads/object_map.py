'''Storage of the xpath, class and id identifiers'''
from easydict import EasyDict

markers = EasyDict({
  'ChatGPT': {
    'login_xq'    : '//button[//div[text()="Log in"]]',
    'continue_xq' : '//button[text()="Continue"]',
    'tutorial_xq' : '//div[contains(text(), "Okay, let’s go")]',
    'button_tq'   : 'button',
    'done_xq'     : '//button[//div[text()="Done"]]',

    'menu_xq'             : '//button[contains(@id, "headlessui-menu-button")]',
    'custom_xq'           : '//a[contains(text(), "Custom instructions")]',
    'custom_toggle_xq'    : '//button[@role="switch"]',
    'custom_textarea_xq'  : '//textarea[@type="button"]',
    'custom_save_xq'      : '//div[contains(text(), "Save")]',
    'custom_cancel_xq'      : '//div[contains(text(), "Cancel")]',
    'custom_tutorial_xq'  : '//div[text()="OK"]',

    'chatbox_xq'  : '//div[@data-message-author-role="assistant"]',
    'wait_xq'     : '//button[@aria-label="Stop generating"]',
    'reset_xq'    : '//a[//span[text()="New chat"]]',
    'reset_cq'    : 'truncate',
    'regen_xq'    : '//div[text()="Regenerate"]',
    'textarea_tq' : 'textarea',
    'textarea_iq' : 'prompt-textarea',
    'gpt_xq'      : '//span[text()="{}"]',
  },

  'HuggingChat': {
    'login_xq'    : '//form[@action="/chat/login"]',
    'username_xq' : '//input[@name="username"]',
    'password_xq' : '//input[@name="password"]',
    'a_login_xq'  : '//button[contains(text(), "Login")]',

    'textarea_xq' : '//textarea[@enterkeyhint="send"]',
    'stop_gen_xq' : '//button[contains(text(),"Stop generating")]',
    'chatbox_xq'  : '//div[@role="presentation"]',
    'search_xq'   : '//div[@aria-label="web search toggle"]',

    'model_xq'    : '//div[div/div/text()="Current Model"]//button',
    'model_li_xq' : '//label',
    'model_a_xq'  : '//button[contains(text(), "Apply")]',
  },

  'Bard': {
    'textarea_xq' : '//div[@role="textbox"]',
    'wait_xq'     : '//img[contains(@src, "sparkle_thinking")]',
    'chatbox_tq'  : 'message-content',
    'search_xq'   : '//div[@aria-label="web search toggle"]',
    'model_xq'    : '//div[div/div/text()="Current Model"]//button',
    'model_li_xq' : '//label',
    'model_a_xq'  : '//button[contains(text(), "Apply")]',
    'new_chat_xq' : '//span[text()="New chat"]',
    'regen_1_xq'  : '//span[text()="View other drafts"]',
    'regen_2_xq'  : '//button[@mattooltip="Regenerate drafts"]'
  }
})
